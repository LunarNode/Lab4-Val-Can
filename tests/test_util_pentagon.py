from NumberGenerator.Sequences.Pentagon import Pentagon
import unittest
import numpy as np
    

class TestUtilsPentagon(unittest.TestCase):
    series = []
    count = 0
    0
    @classmethod
    def setUpClass(cls):
        print("-"*100)
        print("\t\tSTART Pentagon SERIES TEST SCENARIO")
        print("-"*100)
        if len(cls.series)==0:
            Un = Pentagon()
            cls.Un = Un
            cls.series = Un.series
            cls.mean = 0
            cls.median = 0
    def setUp(self):
        TestUtilsPentagon.count+=1
        self.series = TestUtilsPentagon.Un.series
        self.Un = TestUtilsPentagon.Un
        print("TESTCASE: "+str(TestUtilsPentagon.count)+" Executing ...")
        self.get_mean()
        self.get_median()    
    def get_mean(self):
        try:
            self.mean = self.Un.avg
        except AttributeError:
            self.Un.mean()
            self.mean = self.Un.avg
    def get_median(self):
        try:
            self.median = self.Un.median
        except AttributeError:
            self.Un.Median()
            self.median = self.Un.median      
    def test_is_Pentagon_series(self):
        self.assertIsInstance(self.series,list)
        for value in self.series:
            self.assertNotIsInstance(value,str)
            self.assertIsInstance(value,int)
        self.assertIn(len(self.series),[5,6,10,4])
        self.assertNotEqual(len(self.series),0)
        TestUtilsPentagon.series = self.series       
    def test_mean(self):
        self.get_mean()
        sum_of_series = sum(self.series)
        n = len(self.series)
        avg = sum_of_series / n
        self.assertEqual(self.Un.avg,round(avg,2))
        self.assertNotEqual(self.Un.avg,13.5)
        if n==5:self.assertEqual(self.mean,15.0)
        elif n==4:self.assertEqual(self.mean,10.0)
        elif self.Un.lower_bound==5 and self.Un.upper_bound==10:self.assertEqual(self.mean,85.0)
        elif self.Un.lower_bound==1 and self.Un.upper_bound==10:self.assertEqual(self.mean,55.0)
        elif self.Un.lower_bound==15 and self.Un.upper_bound==20:self.assertEqual(self.mean,455.0)
        else:pass
        TestUtilsPentagon.mean = self.mean         
    def test_median(self):
        self.get_median()
        n = len(self.series)
        if n==5:self.assertEqual(self.median,12)
        elif n==4:self.assertEqual(self.median,8.5)
        elif self.Un.lower_bound==5 and self.Un.upper_bound==10:self.assertEqual(self.median,81.0)
        elif self.Un.lower_bound==1 and self.Un.upper_bound==10:self.assertEqual(self.median,43.0)
        elif self.Un.lower_bound==15 and self.Un.upper_bound==20:self.assertEqual(self.median,451.0)
        else:pass
        TestUtilsPentagon.median = self.median  
    def tearDown(self):
        print("TESTCASE: "+str(TestUtilsPentagon.count)+" completed")
    @classmethod
    def tearDownClass(cls):
        print("-"*100)
        print("\t\tSERIES:",cls.series,"\n\t\tMEDIAN:",cls.median,"\n\t\tMEAN:",cls.mean)
        print("\t\tLOWER:",cls.Un.lower_bound,"\n\t\tUPPER:",cls.Un.upper_bound,"\n\t\tCOUNT:",len(cls.Un.series))
        print("-"*100)
        print("\t\tEND OF Pentagon SERIES TEST SCENARIO")
        print("-"*100)
              
if __name__ == '__main__':
    unittest.main(verbosity=3,argv=['first-arg-is-ignored'], Unit=False)
    
    
    
    
    