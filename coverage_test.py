from function_coverage_test import *
from statement_coverage_test import *
from branch_coverage_test import *
from conditional_coverage_test import *
from path_coverage_test import *

import unittest

def my_suite():
    theSuite = unittest.TestSuite()
    theSuite.addTest(unittest.makeSuite(FunctionCoverageTests))
    theSuite.addTest(unittest.makeSuite(StatementCoverageTests))
    theSuite.addTest(unittest.makeSuite(BranchCoverageTests))
    theSuite.addTest(unittest.makeSuite(ConditionalCoverageTests))
    theSuite.addTest(unittest.makeSuite(PathCoverageTests))
    return theSuite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = my_suite()
    runner.run(test_suite)