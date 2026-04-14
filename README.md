\# Doctor Availability \& Booking System



\## Overview

A backend system for managing doctor schedules with recurring availability, date-based overrides, and real-time slot booking.



\## Features



\- Recurring weekly availability (day-based)

\- Date-specific overrides (higher priority)

\- Dynamic 15-minute slot generation

\- Booking system with overlap detection

\- Transaction-safe booking (prevents race conditions)

\- Automatic removal of booked slots from availability



\## Tech Stack



\- Python

\- Django

\- Django REST Framework

\- SQLite



\## API Endpoints



\### Get Availability

GET /api/availability/?doctor\_id=1\&date=YYYY-MM-DD



\### Book Slot

POST /api/book/



\#### Request Body

{

&#x20; "doctor\_id": 1,

&#x20; "date": "2026-04-20",

&#x20; "start\_time": "14:00:00",

&#x20; "end\_time": "14:15:00"

}



\## Key Concepts



\- Override vs recurring priority handling

\- Time slot generation logic

\- Overlap detection using time range conditions

\- Database transactions for safe booking

\- Runtime filtering of booked slots



\## How to Run



1\. Clone repo

2\. Install dependencies:

&#x20;  pip install -r requirements.txt

3\. Run migrations:

&#x20;  python manage.py migrate

4\. Start server:

&#x20;  python manage.py runserver



\## Additional Notes

This project handles real-world scheduling edge cases.

