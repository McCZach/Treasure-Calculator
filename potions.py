import random
from datetime import datetime

class Potion():
    # Key: Tuple - Range of Potion,
    # Value: List [Name, Tuple - Range of XP, Tuple - Range of Gold]
    potion_dict = {}

    @staticmethod
    def build_table():
        temp_dict = {}
        try:
            potion_file = open('tables/potions.txt', 'r')
        except:
            print('Error - Could not open file.')
            return temp_dict
        else:
            line = potion_file.readline().rstrip()
            while line != '':
                potion = line.split(',')

                if line[0] != '?':
                    temp_dict[(int(potion[0]), int(potion[1]))] = list([potion[2], int(potion[3]), int(potion[4])])
                else:
                    temp_dict[(int(potion[0][1::]), int(potion[1]))] = list([potion[2], 
                                (int(potion[3]), int(potion[4])), (int(potion[5]), int(potion[6]))])

                line = potion_file.readline().rstrip()

        potion_file.close()
        return temp_dict

    potion_dict = build_table()

    @staticmethod
    def generate_potion():
        random.seed(str(datetime.now()))
        roll = random.randint(1, 100)

        for potion in Potion.potion_dict:
            min, max = potion
            if roll in range(min, max+1):
                p = potion
                break
        
        # I have the key to the potion
        return f'Potion: {Potion.potion_dict[p][0]}'
