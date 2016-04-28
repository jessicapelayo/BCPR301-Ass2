import unittest
from Model import *


class BranchCoverageTests(unittest.TestCase):
    """
    Test for when all values are true and all values are false
    """

    def setUp(self):
        self.model = Model()

    def tearDown(self):
        print("next")

    def test_true(self):
        """
        50% branch covered
        """
        self.model.data_set = ["A601,M,32,231,Normal,132"]
        self.expected = ["A601,M,32,231,Normal,132"]
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)

    def test_false(self):
        """
        50% branch covered
        """
        self.model.data_set = ["W11,X,111,111,Norm,1234"]
        self.assertTrue(self.model.get_data_set() == self.model.data_set)
        self.expected = []
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)

if __name__ == "__main__":
    unittest.main(verbosity=2)