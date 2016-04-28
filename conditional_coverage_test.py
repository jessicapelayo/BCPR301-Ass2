import unittest
from Model import *


class ConditionalCoverageTests(unittest.TestCase):
    """
    Test to evaluate values against true and false
    """

    def setUp(self):
        self.model = Model()

    def tearDown(self):
        print("next")


    def test_true_false(self):
        """
        50% branch covered
        """
        self.model.validator.data_set = ["J329,N,88,865,Obesity,557"]
        self.assertTrue(self.model.get_data_set() == self.model.validator.data_set)
        self.expected = []
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)

if __name__ == "__main__":
    unittest.main(verbosity=2)