from tables.master import Item

import random
from datetime import datetime

class Potion(Item):
    FILE_PATH = 'resources/potions.txt'
    potion_dict = Item.build_table(FILE_PATH)

    @staticmethod
    def generate_potion():
        random.seed(str(datetime.now()))
        roll = random.randint(1, 100)

        for potion in Potion.potion_dict:
            min, max = potion
            if roll in range(min, max+1):
                p = potion
                break
        
        value = Potion.potion_dict[p]
        if len(value) == 3:
            return f'Potion: {value[0]:28}XP: {value[1]:<13}' + \
                f'Gold: {value[2]:<4}\n'
        else:
            return f'Potion: {value[0]:28}XP: {value[1]}-{value[2]:<9}' + \
                f'Gold: {value[3]}-{value[4]}\n'