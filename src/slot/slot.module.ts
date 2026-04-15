import { Module } from '@nestjs/common';
import { SlotService } from './slot.service';
import { SlotController } from './slot.controller';
import { AppointmentModule } from '../appointment/appointment.module';
import { AvailabilityModule } from '../availability/availability.module';

@Module({
  imports: [AppointmentModule, AvailabilityModule], // ✅ ADD THIS
  controllers: [SlotController],
  providers: [SlotService],
})
export class SlotModule {}