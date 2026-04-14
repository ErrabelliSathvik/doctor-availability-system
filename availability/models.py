from django.db import models
from django.core.exceptions import ValidationError


# ✅ Doctor Model
class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ✅ Recurring Availability
class RecurringAvailability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("Invalid time range")

        overlaps = RecurringAvailability.objects.filter(
            doctor=self.doctor,
            day_of_week=self.day_of_week,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )

        if overlaps.exists():
            raise ValidationError("Overlapping slot")


# ✅ Date Override
class DateOverride(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("Invalid time range")

        overlaps = DateOverride.objects.filter(
            doctor=self.doctor,
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )

        if overlaps.exists():
            raise ValidationError("Overlapping override")


# ✅ Booking Model
class Booking(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("Invalid time")

        overlaps = Booking.objects.filter(
            doctor=self.doctor,
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )

        if self.pk:
            overlaps = overlaps.exclude(pk=self.pk)

        if overlaps.exists():
            raise ValidationError("Slot already booked")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.doctor} | {self.date} | {self.start_time}-{self.end_time}"