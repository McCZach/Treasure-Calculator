from tables.master import Item

import random
from datetime import datetime

class Ring(Item):    
    FILE_PATH = 'resources/rings.txt'
    ring_dict = Item.build_table(FILE_PATH)

    @staticmethod
    def generate_ring():
        random.seed(str(datetime.now()))
        roll = random.randint(1, 100)

        for ring in Ring.ring_dict:
            min, max = ring
            if roll in range(min, max+1):
                r = ring
                break

        value = Ring.ring_dict[r]
        if len(value) == 3:
            return f'Ring: {value[0]:30}XP: {value[1]:<13,}' + \
                f'Gold: {value[2]:<4,}\n'
        else:
            return f'Ring: {value[0]:30}XP: {value[1]}-{value[2]:<8,}' + \
                f'Gold: {value[3]}-{value[4]}\n'
        