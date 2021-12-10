import unittest
from tests.test_util_square import TestUtilsSquare
from tests.test_util_triangle import TestUtilsTriangle
from tests.test_util_pentagon import TestUtilsPentagon
from tests.test_util_normal import TestUtilsNormal
from tests.test_util_uniform import TestUtilsUniform
from tests.test_util_exponential import TestUtilsExponential 

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestUtilsSquare))
    suite.addTest(unittest.makeSuite(TestUtilsTriangle))
    suite.addTest(unittest.makeSuite(TestUtilsPentagon))
    suite.addTest(unittest.makeSuite(TestUtilsExponential))
    suite.addTest(unittest.makeSuite(TestUtilsNormal))
    suite.addTest(unittest.makeSuite(TestUtilsUniform))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    

              
if __name__ == '__main__':
   my_suite()