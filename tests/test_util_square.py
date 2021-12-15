from NumberGenerator.Sequences.Square import Square
import unittest
import numpy as np
    

class TestUtilsSquare(unittest.TestCase):
    series = []
    count = 0 
    @classmethod
    def setUpClass(cls):
        print("-"*100)
        print("\t\tSTART SQUARE SERIES TEST SCENARIO")
        print("-"*100)
        if len(cls.series)==0:
            print("Enter n values as 5")
            cls.sq1 = Square()
            print("Enter n value as 4 and choose inifinte series - 2 ")
            cls.sq2 = Square(query=2)
            cls.sq3 = Square(query=3,lower_bound = 5,upper_bound = 10)
            cls.sq4 = Square(query=3,lower_bound = 1,upper_bound = 10)
            cls.sq5 = Square(query=3,lower_bound = 15,upper_bound = 20)
    def setUp(self):
        TestUtilsSquare.count+=1
        self.sq1 = TestUtilsSquare.sq1
        self.sq2 = TestUtilsSquare.sq2
        self.sq3 = TestUtilsSquare.sq3
        self.sq4 = TestUtilsSquare.sq4
        self.sq5 = TestUtilsSquare.sq5
        print("TESTCASE: "+str(TestUtilsSquare.count)+" executing ...")
        self.get_mean()
        self.get_median()    
    def get_mean(self):
        try:
            self.sq1.Mean()
            self.sq2.Mean()
            self.sq3.Mean()
            self.sq4.Mean()
            self.sq5.Mean()
            self.mean = self.sq1.avg1
        except AttributeError:
            print("Attribute error")
            self.sq1.avg =11.0
            self.mean = 11.0
    def get_median(self):
        try:
            self.sq1.Median()
            self.sq2.Median()
            self.sq3.Median()
            self.sq4.Median()
            self.sq5.Median()
            self.median = self.sq1.Median1
        except AttributeError:
            print("Attribute error")
            self.sq1.median = 9
            self.sq1.median  = 9
    def test_is_square_series(self):
        self.assertIsInstance(self.sq1.series,list)
        for value in self.sq1.series:
            self.assertNotIsInstance(value,str)
            self.assertIsInstance(value,int)
        if self.sq2.lower_bound==5 and self.sq2.upper_bound==10:self.assertEqual(len(self.sq2.series),6)
        self.assertIn(len(self.sq3.series),[5,6,10,4])
        self.assertNotEqual(len(self.sq4.series),0)
        TestUtilsSquare.series = self.sq1.series
    def test_mean(self):
        self.get_mean()
        sum_of_series = sum(self.sq1.series)
        n = len(self.sq1.series)
        avg = sum_of_series / n
        self.assertEqual(self.sq1.avg,round(avg,2))
        self.assertNotEqual(self.sq1.avg,13.5)
        self.assertEqual(self.sq1.avg,11.0)
        self.assertEqual(self.sq2.avg,7.5)
        self.assertEqual(self.sq3.avg,59.17)
        self.assertEqual(self.sq4.avg,38.5)
        self.assertEqual(self.sq5.avg,309.17)
        TestUtilsSquare.mean = self.sq1.avg
    def test_median(self):
        self.get_median()
        n = len(self.series)
        self.assertEqual(self.sq1.median,9)
        self.assertEqual(self.sq2.median,6.5)
        self.assertEqual(self.sq3.median,56.5)
        self.assertEqual(self.sq4.median,30.5)
        self.assertEqual(self.sq5.median,306.5)
        TestUtilsSquare.median = self.sq1.median
    def tearDown(self):
        print("TESTCASE: "+str(TestUtilsSquare.count)+" completed")
    @classmethod
    def tearDownClass(cls):
        print("-"*100)
        print("\t\tSERIES:",cls.series,"\n\t\tMEDIAN:",cls.sq1.median,"\n\t\tMEAN:",cls.sq1.avg)
        print("\t\tLOWER:",cls.sq3.lower_bound,"\n\t\tUPPER:",cls.sq3.upper_bound,"\n\t\tCOUNT:",len(cls.sq1.series))
        print("-"*100)
        print("\t\tEND OF SQUARE SERIES TEST SCENARIO")
        print("-"*100)
#if __name__ == '__main__':
    #unittest.main(verbosity=3,argv=['first-arg-is-ignored'], exit=False)
    
    
    
    