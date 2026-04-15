import { Controller, Get, Query } from '@nestjs/common';
import { SlotService } from './slot.service';
import { AppointmentService } from '../appointment/appointment.service';
import { AvailabilityService } from '../availability/availability.service';

@Controller('slots')
export class SlotController {
  constructor(
    private readonly slotService: SlotService,
    private readonly appointmentService: AppointmentService,
    private readonly availabilityService: AvailabilityService, // ✅ FIXED
  ) {}

  @Get()
  getSlots(
    @Query('doctorId') doctorId: string,
    @Query('date') date: string,
  ) {
    const availability = this.availabilityService.getAvailability(doctorId, date);

    if (!availability) return [];

    const start = new Date(date);
    start.setHours(availability.startHour, 0, 0);

    const end = new Date(date);
    end.setHours(availability.endHour, 0, 0);

    const slots = this.slotService.generateSlots(start, end, 15);

    const appointments = this.appointmentService['appointments'];

    return slots.filter(slot =>
      !appointments.some(app =>
        app.doctorId === doctorId &&
        slot.start < app.end &&
        slot.end > app.start
      )
    );
  }
}