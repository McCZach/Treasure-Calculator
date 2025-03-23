import random
from datetime import datetime

class Ring():
    @staticmethod
    def build_table():
        temp_dict = {}
        try:
            ring_file = open('resources/rings.txt', 'r')
        except:
            print('Error - Could not open file.')
            return temp_dict
        else:
            line = ring_file.readline().rstrip()
            while line != '':
                ring = line.split(',')

                if line[0] != '?':
                    temp_dict[(int(ring[0]), int(ring[1]))] = list([ring[2], int(ring[3]), int(ring[4])])
                else:
                    temp_dict[(int(ring[0][1::]), int(ring[1]))] = list([ring[2], 
                                    int(ring[3]), int(ring[4]), int(ring[5]), int(ring[6])])

                line = ring_file.readline().rstrip()
        
        ring_file.close()
        return temp_dict

    ring_dict = build_table()

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
            return f'Ring: {value[0]:30}XP: {value[1]:<10}' + \
                f'Gold: {value[2]:<4}\n'
        else:
            return f'Ring: {value[0]:30}XP: {value[1]}-{value[2]:<5}' + \
                f'Gold: {value[3]}-{value[4]}\n'
        