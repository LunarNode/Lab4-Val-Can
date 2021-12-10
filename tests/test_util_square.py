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
            sq = Square()
            cls.sq = sq
            cls.series = sq.series                  
    def setUp(self):
        TestUtilsSquare.count+=1
        self.series = TestUtilsSquare.sq.series
        self.sq = TestUtilsSquare.sq
        print("TESTCASE: "+str(TestUtilsSquare.count)+" executing ...")
        self.get_mean()
        self.get_median()    
    def get_mean(self):
        try:
            self.mean = self.sq.avg
        except AttributeError:
            self.sq.mean()
            self.mean = self.sq.avg
    def get_median(self):
        try:
            self.median = self.sq.median
        except AttributeError:
            self.sq.Median()
            self.median = self.sq.median      
    def test_is_square_series(self):
        self.assertIsInstance(self.series,list)
        for value in self.series:
            self.assertNotIsInstance(value,str)
            self.assertIsInstance(value,int)
        if self.sq.lower_bound==5 and self.sq.upper_bound==10:self.assertEqual(len(self.series),6)
        self.assertIn(len(self.series),[5,6,10,4])
        self.assertNotEqual(len(self.series),0)
        TestUtilsSquare.series = self.series       
    def test_mean(self):
        self.get_mean()
        sum_of_series = sum(self.series)
        n = len(self.series)
        avg = sum_of_series / n
        self.assertEqual(self.sq.avg,round(avg,2))
        self.assertNotEqual(self.sq.avg,13.5)
        if n==5:self.assertEqual(self.mean,11.0)
        elif n==4:self.assertEqual(self.mean,7.5)
        elif self.sq.lower_bound==5 and self.sq.upper_bound==10:self.assertEqual(self.mean,59.17)
        elif self.sq.lower_bound==1 and self.sq.upper_bound==10:self.assertEqual(self.mean,38.5)
        elif self.sq.lower_bound==15 and self.sq.upper_bound==20:self.assertEqual(self.mean,309.17)
        else:pass
        TestUtilsSquare.mean = self.mean         
    def test_median(self):
        self.get_median()
        n = len(self.series)
        if n==5:self.assertEqual(self.median,9)
        elif n==4:self.assertEqual(self.median,6.5)
        elif self.sq.lower_bound==5 and self.sq.upper_bound==10:self.assertEqual(self.median,56.5)
        elif self.sq.lower_bound==1 and self.sq.upper_bound==10:self.assertEqual(self.median,30.5)
        elif self.sq.lower_bound==15 and self.sq.upper_bound==20:self.assertEqual(self.median,306.5)
        else:pass
        TestUtilsSquare.median = self.median  
    def tearDown(self):
        print("TESTCASE: "+str(TestUtilsSquare.count)+" completed")
    @classmethod
    def tearDownClass(cls):
        print("-"*100)
        print("\t\tSERIES:",cls.series,"\n\t\tMEDIAN:",cls.median,"\n\t\tMEAN:",cls.mean)
        print("\t\tLOWER:",cls.sq.lower_bound,"\n\t\tUPPER:",cls.sq.upper_bound,"\n\t\tCOUNT:",len(cls.sq.series))
        print("-"*100)
        print("\t\tEND OF SQUARE SERIES TEST SCENARIO")
        print("-"*100)
              
if __name__ == '__main__':
    unittest.main(verbosity=3,argv=['first-arg-is-ignored'], exit=False)
    
    
    
    