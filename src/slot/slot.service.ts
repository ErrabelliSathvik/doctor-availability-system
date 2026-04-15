import { Injectable } from '@nestjs/common';

type Slot = {
  start: Date;
  end: Date;
};

@Injectable()
export class SlotService {
  generateSlots(start: Date, end: Date, duration: number): Slot[] {
    const slots: Slot[] = [];
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