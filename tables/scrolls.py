from tables.armor import Item

import random
from datetime import datetime

class Scroll(Item):
    FILE_PATH = 'resources/scrolls.txt'
    scroll_dict = Item.build_table(FILE_PATH)

    @staticmethod
    def generate_scroll() -> str:
        random.seed(str(datetime.now()))
        roll = random.randint(1, 100)

        for scroll in Scroll.scroll_dict:
            min, max = scroll
            if roll in range(min, max+1):
                s = scroll
                break

        value = Scroll.scroll_dict[s]
        return f'Scroll: {value[0]:43}Spell Level Range: {value[1]:<13}\n'