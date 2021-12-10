from NumberGenerator.Distributions.exponential import Exponential
import unittest
import numpy as np
    

class TestUtilsExponential(unittest.TestCase):
    lst = []
    count = 0 
    @classmethod
    def setUpClass(cls):
        print("-"*100)
        print("\t\tSTART Exponential Distribution TEST SCENARIO")
        print("-"*100)
        if len(cls.lst)==0:
            Ex = Exponential()
            Ex.generate(0.1,100)
            cls.Ex = Ex
            cls.lst = Ex.lst   
            cls.mean = cls.Ex.get_mean()
            cls.var = cls.Ex.get_var()               
    def setUp(self):
        print(type(self.lst))
        TestUtilsExponential.count+=1
        self.lst = TestUtilsExponential.Ex.lst
        self.Ex = TestUtilsExponential.Ex
        print("TESTCASE: "+str(TestUtilsExponential.count)+" executing ...")
        self.mean = self.Ex.get_mean()
        self.var = self.Ex.get_var()    
    
    def test_is_Exponential_lst(self):
        self.assertEqual(type(self.lst),type(np.array(10)))
        for value in self.lst:
            self.assertNotIsInstance(value,str)
            self.assertIsInstance(value,float)
        self.assertNotEqual(len(self.lst),1000)
        self.assertNotEqual(len(self.lst),0)
        
    def test_mean(self):
        sum_of_lst = sum(self.lst)
        n = len(self.lst)
        mean = sum_of_lst / n
        self.assertEqual(round(self.Ex.mean,2),round(mean,2))
        self.assertNotEqual(self.Ex.mean,13.5)
        self.assertNotEqual(round(self.mean,2),0.9)
        self.assertEqual(int(self.mean%2),0)
        self.assertNotIsInstance(self.mean,int)
        TestUtilsExponential.mean = self.mean         
    def test_var(self):
        self.var = self.Ex.get_var()
        n = len(self.lst)
        self.assertTrue(round(self.var,2) < 1 and round(self.var,2) >= 0  )
        self.assertTrue(int(round(self.var,2)*100) != 100 )
        self.assertNotIsInstance(self.var,int)
        self.assertIsInstance(self.var,float)
        self.assertEqual(int(self.var%2),0)
        TestUtilsExponential.var = self.var  
    def tearDown(self):
        print("TESTCASE: "+str(TestUtilsExponential.count)+" completed")
    @classmethod
    def tearDownClass(cls):
        print("-"*100)
        print("\n\t\tVARIANCE:",cls.var,"\n\t\tMEAN:",cls.mean)
        print("-"*100)
        print("\t\tEND OF Exponential Distribution TEST SCENARIO")
        print("-"*100)
              
if __name__ == '__main__':
    unittest.main(verbosity=3,argv=['first-arg-is-ignored'], exit=False)
    
    
    
    