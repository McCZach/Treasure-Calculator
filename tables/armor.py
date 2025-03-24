from tables.master import Item

import random
from datetime import datetime

class Armor(Item):
    FILE_PATH = 'resources/armor.txt'
    armor_dict = Item.build_table(FILE_PATH)

    @staticmethod
    def generate_armor():
        random.seed(str(datetime.now()))
        roll = random.randint(1, 100)

        for armor in Armor.armor_dict:
            min, max = armor
            if roll in range(min, max+1):
                a = armor
                break

        value = Armor.armor_dict[a]
        return f'Armor: {value[0]:<44}XP: {value[1]:<15}Gold: {value[2]}\n'