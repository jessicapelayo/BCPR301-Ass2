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


class Model:
    def __init__(self):
        self.data_set = list()
        self.good_data = {}
        self.display_data = list()
        self.wrong_data = list()
        self.file_there = ""

    def add_new_data(self, new_array):
        # try catch if its a list
        self.data_set += new_array

    def del_data(self):
        self.data_set = list()

    def get_data_set(self):
        return self.data_set

    def get_data(self):
        return self.display_data

    def read_in_csv(self, path):
        print("loading file...")
        file = open(path)
        txt = file.read()
        li = txt.split('\n')
        if li[-1].strip() == '':
            del li[-1]
        self.add_new_data(li)
        if self.data_set is not []:
            print("File Loaded!")
        #self.wash_data()

    def wash_data(self):
        #self.loop_lines()
        for line in self.data_set:
            self.loop_line_item(line)
        return self.get_good_data()

    def get_good_data(self):
        result = []
        for i in self.good_data:
            p = self.good_data.get(i)
            result.append(i + "," + p.get_gender() + "," + p.get_age() + "," + p.get_sales() + "," + p.get_bmi() + "," + p.get_income())
        return result


    #def loop_lines(self):
    #    for line in self.data_set:
    #        self.loop_line_item(line)


    def loop_line_item(self, line):
        RULES = ['^[A-Z][0-9]{3}$', '(M|F)', '[0-9]{2}$', '[0-9]{3}$', '(Normal|Overweight|Obesity|Underweight)',
                 '[0-9]{2,3}$']
        split_line = line.split(',')
        #for me, this line of code is unnecessary but it is needed for all the get methods to work
        self.display_data.insert(self.display_data.__sizeof__(), split_line)
        i = 0
        num_of_invalid_data = 0
        for item in split_line:
            result = re.match(RULES[i], item)
            i += 1
            #if result == None:
                #self.wrong_data.append(line)
            if result == None:
                num_of_invalid_data += 1
        self.validate_line(line, num_of_invalid_data)

    def validate_line(self, line, aNum):
        if aNum == 0:
            self.good_data_to_obj(line)

    def good_data_to_obj(self, line):
        #self.data_set = list(set(self.data_set) - set(self.wrong_data))
        split_line = line.split(',')
        new_person = Person(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5])
        self.good_data.update({new_person.get_id() : new_person})


    def save_data(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.display_data, f)

    def pickle_data(self):
        try:
            with open('data.pickle', 'rb') as f:
                self.display_data = pickle.load(f)
        except FileNotFoundError:
            print("Existing data not found.")
            return

    def get_sales(self):
        result = []
        for i in self.display_data:
            result.append(int(i[3]))
        return result

    def get_weight(self):
        normal = 0
        over = 0
        obese = 0
        under = 0
        for i in self.display_data:
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
        for i in self.display_data:
            if i[1] == 'M':
                m += 1
            elif i[1] == 'F':
                f += 1
        return [m, f]

