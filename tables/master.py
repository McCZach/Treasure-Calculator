import os
import sys

class Item():
    @staticmethod
    def build_table(file_path: str) -> dict:
        data = {}
        try:
            if hasattr(sys, '_MEIPASS'):
                file_path = os.path.join(sys._MEIPASS, file_path)
            file = open(file_path, 'r')
        except:
            print('Error - Could not open file.')
            return data
        else:
            line = file.readline().rstrip()
            while line != '':
                info = line.split(',')

                if line[0] != '?':
                    data[(int(info[0]), int(info[1]))] = list([info[2], int(info[3]), int(info[4])])
                else:
                    data[(int(info[0][1::]), int(info[1]))] = list([info[2], 
                                    int(info[3]), int(info[4]), int(info[5]), int(info[6])])

                line = file.readline().rstrip()
        
        file.close()
        return data