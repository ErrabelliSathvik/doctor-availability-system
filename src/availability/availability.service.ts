import { Injectable } from '@nestjs/common';

type Availability = {
  doctorId: string;
  dayOfWeek: number;
  startHour: number;
  endHour: number;
};

type CustomAvailability = {
  doctorId: string;
  date: string;
  startHour: number;
  endHour: number;
};

@Injectable()
export class AvailabilityService {
  private recurring: Availability[] = [
    { doctorId: '1', dayOfWeek: 3, startHour: 10, endHour: 14 }, // Wednesday
  ];

  private custom: CustomAvailability[] = [
    { doctorId: '1', date: '2026-04-16', startHour: 14, endHour: 18 },
  ];

  getAvailability(doctorId: string, date: string) {
    const custom = this.custom.find(
      a => a.doctorId === doctorId && a.date === date,
    );

    if (custom) return custom;

    const day = new Date(date).getDay();

    return this.recurring.find(
      a => a.doctorId === doctorId && a.dayOfWeek === day,
    );
  }
}