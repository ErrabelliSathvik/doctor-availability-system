import { Module } from '@nestjs/common';
import { AvailabilityService } from './availability.service';

@Module({
  providers: [AvailabilityService],
  exports: [AvailabilityService], // ✅ VERY IMPORTANT
})
export class AvailabilityModule {}