import unittest
from Model import *


class StatementCoverageTests(unittest.TestCase):
    """
    Testing when all values are true (i.e. all inputs are correct)
    """

    def setUp(self):
        self.model = Model()

    def tearDown(self):
        print("next")

    def test_wash_data(self):
        """
            100% statement covered
        """
        self.model.validator.data_set = ["A601,M,32,231,Normal,132"]
        self.expected = ["A601,M,32,231,Normal,132"]
        self.actual = self.model.wash_data()
        self.assertTrue(self.expected == self.actual)

if __name__ == "__main__":
    unittest.main(verbosity=2)