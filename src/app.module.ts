import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SlotModule } from './slot/slot.module';

@Module({
  imports: [SlotModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
