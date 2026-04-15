import { Controller, Post, Body } from '@nestjs/common';
import { AppointmentService } from './appointment.service';

@Controller('appointment')
export class AppointmentController {
  constructor(private readonly service: AppointmentService) {}

  @Post()
  book(@Body() body) {
    const { doctorId, start, end } = body;

    return this.service.bookSlot(
      doctorId,
      new Date(start),
      new Date(end),
    );
  }
}
