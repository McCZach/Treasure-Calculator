from tables.master import Item

import random
from datetime import datetime

class Wand(Item):
    FILE_PATH = 'resources/wands.txt'
    wand_dict = Item.build_table(FILE_PATH)

    @staticmethod
    def generate_wand():
        random.seed(str(datetime.now()))
        roll = random.randint(1, 100)

        for wand in Wand.wand_dict:
            min, max = wand
            if roll in range(min, max+1):
                w = wand
                break

        value = Wand.wand_dict[w]
        return f'Item: {value[0]:45}XP: {value[1]:<15}Gold: {value[2]}\n'