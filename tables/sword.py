from tables.armor import Item

import random
from datetime import datetime

class Sword(Item):
    FILE_PATH = 'resources/swords.txt'
    sword_dict = Item.build_table(FILE_PATH)

    @staticmethod
    def generate_sword() -> str:
        random.seed(str(datetime.now()))
        roll = random.randint(1, 100)

        for sword in Sword.sword_dict:
            min, max = sword
            if roll in range(min, max+1):
                s = sword
                break
        
        value = Sword.sword_dict[s]
        return f'Sword: {value[0]:<44}XP: {value[1]:<15}Gold: {value[2]}\n'