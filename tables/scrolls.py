import random
from datetime import datetime

class Scroll():
    @staticmethod
    def build_table():
        data = {}
        try:
            file = open('resources/scrolls.txt', 'r')
        except:
            print('Error - Could not open file.')
            return data
        else:
            line = file.readline().rstrip()
            while line != '':
                info = line.split(',')
                data[(int(info[0]), int(info[1]))] = list([info[2], info[3]])

                line = file.readline().rstrip()

        file.close()
        return data

    scroll_dict = build_table()

    @staticmethod
    def generate_scroll():
        random.seed(str(datetime.now()))
        roll = random.randint(1, 100)

        for scroll in Scroll.scroll_dict:
            min, max = scroll
            if roll in range(min, max+1):
                s = scroll
                break

        value = Scroll.scroll_dict[s]
        return f'Scroll: {value[0]:43}Spell Level Range: {value[1]:<13}\n'