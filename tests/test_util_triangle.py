from NumberGenerator.Sequences.Triangle import Triangle
import unittest
import numpy as np
    

class TestUtilsTriangle(unittest.TestCase):
    series = []
    count = 0 
    @classmethod
    def setUpClass(cls):
        print("-"*100)
        print("\t\tSTART TRIANGLE SERIES TEST SCENARIO")
        print("-"*100)
        if len(cls.series)==0:
            Tri = Triangle()
            cls.Tri = Tri
            cls.series = Tri.series
            cls.median = 0
            cls.mean = 0
    def setUp(self):
        TestUtilsTriangle.count+=1
        self.series = TestUtilsTriangle.Tri.series
        self.Tri = TestUtilsTriangle.Tri
        print("TESTCASE: "+str(TestUtilsTriangle.count)+" executing ...")
        self.get_mean()
        self.get_median()    
    def get_mean(self):
        try:
            self.mean = self.Tri.avg
        except AttributeError:
            self.Tri.mean()
            self.mean = self.Tri.avg
    def get_median(self):
        try:
            self.median = self.Tri.median
        except AttributeError:
            self.Tri.Median()
            self.median = self.Tri.median      
    def test_is_Triangle_series(self):
        self.assertIsInstance(self.series,list)
        for value in self.series:
            self.assertNotIsInstance(value,str)
            self.assertIsInstance(value,int)
        self.assertNotEqual(len(self.series),100)
        self.assertNotEqual(len(self.series),0)
        TestUtilsTriangle.series = self.series       
    def test_mean(self):
        self.get_mean()
        sum_of_series = sum(self.series)
        n = len(self.series)
        avg = sum_of_series / n
        self.assertEqual(self.Tri.avg,round(avg,2))
        self.assertNotEqual(self.Tri.avg,13.5)
        if n==5:self.assertEqual(self.mean,7.0)
        elif n==4:self.assertEqual(self.mean,5.0)
        elif self.Tri.lower_bound==5 and self.Tri.upper_bound==10:self.assertEqual(self.mean,33.33)
        elif self.Tri.lower_bound==1 and self.Tri.upper_bound==10:self.assertEqual(self.mean,22.0)
        elif self.Tri.lower_bound==15 and self.Tri.upper_bound==20:self.assertEqual(self.mean,163.33)
        else:pass
        TestUtilsTriangle.mean = self.mean         
    def test_median(self):
        self.get_median()
        n = len(self.series)
        if n==5:self.assertEqual(self.median,6)
        elif n==4:self.assertEqual(self.median,4.5)
        elif self.Tri.lower_bound==5 and self.Tri.upper_bound==10:self.assertEqual(self.median,32.0)
        elif self.Tri.lower_bound==1 and self.Tri.upper_bound==10:self.assertEqual(self.median,18.0)
        elif self.Tri.lower_bound==15 and self.Tri.upper_bound==20:self.assertEqual(self.median,162.0)
        else:pass
        TestUtilsTriangle.median = self.median  
    def tearDown(self):
        print("TESTCASE: "+str(TestUtilsTriangle.count)+" completed")
    @classmethod
    def tearDownClass(cls):
        print("-"*100)
        print("\t\tSERIES:",cls.series,"\n\t\tMEDIAN:",cls.median,"\n\t\tMEAN:",cls.mean)
        print("\t\tLOWER:",cls.Tri.lower_bound,"\n\t\tUPPER:",cls.Tri.upper_bound,"\n\t\tCOUNT:",len(cls.series))
        print("-"*100)
        print("\t\tEND OF Triangle SERIES TEST SCENARIO")
        print("-"*100)
              
if __name__ == '__main__':
    unittest.main(verbosity=3,argv=['first-arg-is-ignored'], Unit=False)
    
    
    
    
    