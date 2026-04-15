import { Injectable } from '@nestjs/common';

@Injectable()
export class SlotService {
  generateSlots(start: Date, end: Date, duration: number) {
    const slots = [];
    let current = new Date(start);

    while (current.getTime() + duration * 60000 <= end.getTime()) {
      const slotEnd = new Date(current.getTime() + duration * 60000);

      slots.push({
        start: new Date(current),
        end: slotEnd,
      });

      current = slotEnd;
    }

    return slots;
  }
}