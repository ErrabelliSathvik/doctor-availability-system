# Doctor Availability & Slot Booking System

## Overview
This project implements a backend system to generate bookable time slots for doctors based on availability and allows patients to book appointments.

---

## Features

- Recurring availability (weekly schedule)
- Custom date availability override
- Dynamic slot generation (configurable duration)
- Conflict-free booking (no overlapping appointments)
- Only future available slots returned

---

## Tech Stack

- NestJS (Backend framework)
- Prisma (ORM)
- PostgreSQL (Database)

---

## System Design

### Availability Resolution
- If custom availability exists → use it
- Else → fallback to recurring availability

### Slot Generation
- Slots generated dynamically from start to end time
- Ensures no overflow beyond availability window

### Booking Logic
- Prevents overlapping appointments using time interval checks

---

## API Endpoints

### Get Available Slots
GET /slots?doctorId=1&date=YYYY-MM-DD

### Add Recurring Availability
POST /availability/recurring

### Add Custom Availability
POST /availability/custom

### Book Appointment
POST /appointment

---

## Setup

```bash
npm install
npm run start:dev

---

# ⚙️ What to do now

1. Replace your README with above content  
2. Save  
3. Commit:

```bash
git add .
git commit -m "improved README with system explanation"
git push origin task-slot-booking
## Slot Logic
Slots are generated dynamically using time intervals.