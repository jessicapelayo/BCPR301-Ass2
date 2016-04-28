"""
    >>> myModel = Model()
    >>> myModel.read_in_csv("TestData.csv")
    loading file...
    File Loaded!

    >>> integer = myModel.wash_data().__len__()
    >>> integer
    7


"""
import re
import pickle
from Person import *
from Validator import *


class Model:
    def __init__(self):
        self.file_there = ""
        self.validator = Validator()

    def add_new_data(self, new_array):
        self.validator.add_new_data(new_array)

    def del_data(self):
        self.validator.del_data()

    def get_data_set(self):
        return self.validator.get_data_set()


    def read_in_csv(self, path):
        print("loading file...")
        file = open(path)
        txt = file.read()
        li = txt.split('\n')
        if li[-1].strip() == '':
            del li[-1]
        self.add_new_data(li)
        if self.validator.get_data_set() is not []:
            print("File Loaded!")
        #self.wash_data()

    def wash_data(self):
        return self.validator.wash_data()

    def save_data(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.validator.get_data(), f)

    def get_sales(self):
        result = []
        for i in self.validator.get_data():
            result.append(int(i[3]))
        return result

    def get_weight(self):
        normal = 0
        over = 0
        obese = 0
        under = 0
        for i in self.validator.get_data():
            if i[4] == 'Normal':
                normal += 1
            elif i[4] == 'Overweight':
                over += 1
            elif i[4] == 'Obesity':
                obese += 1
            elif i[4] == 'Underweight':
                under += 1
        return [normal, over, obese, under]

    def get_gender(self):
        m = 0
        f = 0
        for i in self.validator.get_data():
            if i[1] == 'M':
                m += 1
            elif i[1] == 'F':
                f += 1
        return [m, f]

