import unittest
from Model import *

class FunctionCoverageTests(unittest.TestCase):
    """
    Testing functionality
    """

    def setUp(self):
        self.model = Model()

    def tearDown(self):
        print("next")

    def test_read_in_csv(self):
        self.model.read_in_csv("testFileLoad.txt")
        self.expected = ['Hello This Is A Test', 'Hello This is Another Test']
        self.actual = self.model.get_data_set()
        print(self.actual)
        self.assertTrue(self.expected == self.actual)

    def test_wash_data(self):
        self.model.read_in_csv("TestData.csv")
        #self.model.wash_data()
        self.expected = 7
        self.actual = self.model.wash_data().__len__()
        print(self.model.wash_data())
        self.assertTrue(self.expected == self.actual)

    def test_get_sales(self):
        self.model.read_in_csv("TestData.csv")
        self.model.wash_data()
        self.expected = [312, 231, 231, 245, 63, 764, 636, 133, 878, 678, 865, 345]
        #self.expected = [231, 764, 636, 133, 678, 345]
        self.actual = self.model.get_sales()
        #print(self.model.get_sales())
        self.assertTrue(self.expected == self.actual)

    def test_get_weight(self):
        self.model.read_in_csv("TestData.csv")
        self.model.wash_data()
        self.expected = [4, 1, 2, 4]
        self.actual = self.model.get_weight()
        print(self.model.get_weight())
        self.assertTrue(self.expected == self.actual)

    def test_get_gender(self):
        self.model.read_in_csv("TestData.csv")
        self.model.wash_data()
        self.expected = [4, 7]
        self.actual = self.model.get_gender()
        print(self.model.get_gender())
        self.assertTrue(self.expected == self.actual)

if __name__ == "__main__":
    unittest.main(verbosity=2)