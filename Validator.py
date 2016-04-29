import re
from Person import *

class Validator:
    def __init__(self):
        self.data_set = list()
        self.good_data = {}
        self.display_data = list()

    def get_data_set(self):
     return self.data_set

    def get_data(self):
        return self.display_data

    def add_new_data(self, new_array):
        #try catch if its a list
        self.data_set += new_array

    def del_data(self):
        self.data_set = list()

    def wash_data(self):
        for line in self.data_set:
            self.loop_line_item(line)
        return self.get_good_data()

    def get_good_data(self):
        result = []
        for i in self.good_data:
            p = self.good_data.get(i)
            result.append(
                i + "," + p.get_gender() + "," + p.get_age() + "," + p.get_sales() + "," + p.get_bmi() + "," + p.get_income())
        return result

    def loop_line_item(self, line):
        RULES = ['^[A-Z][0-9]{3}$', '(M|F)', '[0-9]{2}$', '[0-9]{3}$', '(Normal|Overweight|Obesity|Underweight)',
                 '[0-9]{2,3}$']
        split_line = line.split(',')
        # for me, this line of code is unnecessary but it is needed for all the get methods to work
        self.display_data.insert(self.display_data.__sizeof__(), split_line)
        i = 0
        num_of_invalid_data = 0
        for item in split_line:
            result = re.match(RULES[i], item)
            i += 1
            if result == None:
                num_of_invalid_data += 1
        self.validate_line(line, num_of_invalid_data)

    def validate_line(self, line, a_num):
        if a_num == 0:
            self.good_data_to_obj(line)

    def good_data_to_obj(self, line):
        split_line = line.split(',')
        new_person = Person(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5])
        self.good_data.update({new_person.get_id(): new_person})
