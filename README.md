# 🩺 Doctor Availability & Slot Booking System

A backend system built using NestJS that dynamically generates bookable time slots based on doctor availability and ensures conflict-free appointment booking.

---

## 🚀 Features

- ⏱️ Dynamic slot generation based on time intervals
- 📅 Support for recurring weekly availability
- 📌 Custom date-based availability override
- ❌ Conflict-free booking using interval overlap detection
- 🔄 Automatic filtering of already booked slots
- ⚙️ Configurable slot duration (e.g., 15 mins)

---

## 🧠 Core Logic

### 🔹 Availability Resolution
- If custom availability exists for a date → use it
- Else → fallback to recurring weekly availability

### 🔹 Conflict Detection
Prevents double booking using interval overlap logic:
start < existingEnd && end > existingStart

## 🏗️ Project Structure


src/
├── slot/ # Slot generation logic
├── appointment/ # Booking logic
├── availability/ # Availability + override logic


---

## ⚙️ Tech Stack

- NestJS
- TypeScript
- Node.js

---

## 📡 API Endpoints

### 🔹 Get Available Slots


GET /slots?doctorId=1&date=2026-04-16


#### Response:
```json
[
  {
    "start": "2026-04-16T08:30:00.000Z",
    "end": "2026-04-16T08:45:00.000Z"
  }
]
🔹 Book Appointment
POST /appointment
Request Body:
{
  "doctorId": "1",
  "start": "2026-04-16T08:30:00.000Z",
  "end": "2026-04-16T08:45:00.000Z"
}