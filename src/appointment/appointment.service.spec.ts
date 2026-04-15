import { Injectable } from '@nestjs/common';

type Appointment = {
  doctorId: string;
  start: Date;
  end: Date;
};

@Injectable()
export class AppointmentService {
  private appointments: Appointment[] = [];

  bookSlot(doctorId: string, start: Date, end: Date) {
    const conflict = this.appointments.find(app =>
      app.doctorId === doctorId &&
      start < app.end &&
      end > app.start
    );

    if (conflict) {
      throw new Error('Slot already booked');
    }

    const newAppointment: Appointment = { doctorId, start, end };
    this.appointments.push(newAppointment);

    return newAppointment;
  }
}