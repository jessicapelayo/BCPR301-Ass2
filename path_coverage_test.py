import unittest
from Model import *


class PathCoverageTests(unittest.TestCase):
    """
    Test each path of the decision
    """

    def setUp(self):
        self.model = Model()

    def tearDown(self):
        print("next")


    def test_1_tttttf(self):
        self.model.data_set = ["A601,M,32,231,Normal,1234"]
        self.assertTrue(self.model.get_data_set() == self.model.data_set)
        self.expected = []
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)

    def test_3_ttttft(self):
        self.model.data_set = ["A601,M,32,231,Nor,132"]
        self.assertTrue(self.model.get_data_set() == self.model.data_set)
        self.expected = []
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)

    def test_4_tttftt(self):
        self.model.data_set = ["A601,M,32,1234,Normal,132"]
        self.assertTrue(self.model.get_data_set() == self.model.data_set)
        self.expected = []
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)

    def test_5_ttfttt(self):
        self.model.data_set = ["A601,M,111f,123,Normal,123"]
        self.assertTrue(self.model.get_data_set() == self.model.data_set)
        self.expected = []
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)


    def test_6_tftttt(self):
        self.model.data_set = ["A601,N,32,123,Normal,123"]
        self.assertTrue(self.model.get_data_set() == self.model.data_set)
        self.expected = []
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)

    def test_7_fttttt(self):
        self.model.data_set = ["0000,N,32,123,Normal,123"]
        self.assertTrue(self.model.get_data_set() == self.model.data_set)
        self.expected = []
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)




if __name__ == "__main__":
    unittest.main(verbosity=2)