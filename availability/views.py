from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta

from django.db import transaction
from django.core.exceptions import ValidationError

from .models import RecurringAvailability, DateOverride, Booking


# 🔹 Generate slots (15 mins)
def generate_slots(start_time, end_time, slot_minutes=15):
    slots = []

    start = datetime.combine(datetime.today(), start_time)
    end = datetime.combine(datetime.today(), end_time)

    while start < end:
        slot_end = start + timedelta(minutes=slot_minutes)

        # prevent overflow
        if slot_end > end:
            break

        slots.append({
            "start_time": start.time().strftime("%H:%M:%S"),
            "end_time": slot_end.time().strftime("%H:%M:%S")
        })

        start = slot_end

    return slots


# 🔹 Core availability logic
def get_availability(doctor_id, date):

    overrides = DateOverride.objects.filter(
        doctor_id=doctor_id,
        date=date
    )

    slots = []

    # Step 1: Generate slots
    if overrides.exists():
        for o in overrides:
            slots.extend(generate_slots(o.start_time, o.end_time))
    else:
        day = date.weekday()

        recurring = RecurringAvailability.objects.filter(
            doctor_id=doctor_id,
            day_of_week=day
        )

        for r in recurring:
            slots.extend(generate_slots(r.start_time, r.end_time))

    # Step 2: Fetch booked slots
    bookings = Booking.objects.filter(
        doctor_id=doctor_id,
        date=date
    )

    booked_slots = set()
    for b in bookings:
        booked_slots.add((
            b.start_time.strftime("%H:%M:%S"),
            b.end_time.strftime("%H:%M:%S")
        ))

    # Step 3: Remove booked slots
    available_slots = [
        slot for slot in slots
        if (slot["start_time"], slot["end_time"]) not in booked_slots
    ]

    return available_slots


# 🔹 GET availability API
@api_view(['GET'])
def availability_view(request):
    doctor_id = request.GET.get('doctor_id')
    date_str = request.GET.get('date')

    if not doctor_id or not date_str:
        return Response({"error": "doctor_id and date required"}, status=400)

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return Response({"error": "Invalid date format (YYYY-MM-DD)"}, status=400)

    data = get_availability(doctor_id, date)

    return Response(data)


# 🔹 POST booking API (SAFE with transaction)
@api_view(['POST'])
def book_slot(request):
    doctor_id = request.data.get('doctor_id')
    date = request.data.get('date')
    start_time = request.data.get('start_time')
    end_time = request.data.get('end_time')

    if not all([doctor_id, date, start_time, end_time]):
        return Response({"error": "All fields required"}, status=400)

    try:
        with transaction.atomic():

            booking = Booking(
                doctor_id=doctor_id,
                date=date,
                start_time=start_time,
                end_time=end_time
            )

            # validation (overlap check)
            booking.full_clean()

            booking.save()

            return Response({"message": "Booked successfully"})

    except ValidationError as e:
        return Response({"error": str(e)}, status=400)

    except Exception:
        return Response({"error": "Something went wrong"}, status=500)