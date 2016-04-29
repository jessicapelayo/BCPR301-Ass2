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
from ChartData import *


class Model:
    def __init__(self):
        self.file_there = ""
        self.validator = Validator()
        self.chart_data = ChartData()

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
        return self.chart_data.get_sales(self.validator.get_data())

    def get_weight(self):
        return self.chart_data.get_weight(self.validator.get_data())

    def get_gender(self):
        return self.chart_data.get_gender(self.validator.get_data())