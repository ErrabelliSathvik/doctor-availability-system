import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SlotModule } from './slot/slot.module';
import { AppointmentModule } from './appointment/appointment.module';
import { AvailabilityModule } from './availability/availability.module';

@Module({
  imports: [SlotModule, AppointmentModule, AvailabilityModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
