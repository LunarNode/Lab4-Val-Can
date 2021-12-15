from NumberGenerator.Sequences.Pentagon import Pentagon
import unittest
import numpy as np


class TestUtilsPentagon(unittest.TestCase):
    series = []
    count = 0

    @classmethod
    def setUpClass(cls):
        print("-" * 100)
        print("\t\tSTART Pentagon SERIES TEST SCENARIO")
        print("-" * 100)
        if len(cls.series) == 0:
            print("Enter n values as 5")
            cls.pen1 = Pentagon()
            cls.pen2 = Pentagon(query=2)
            cls.pen3 = Pentagon(query=3, lower_bound=5, upper_bound=10)
            cls.pen4 = Pentagon(query=3, lower_bound=1, upper_bound=10)
            cls.pen5 = Pentagon(query=3, lower_bound=15, upper_bound=20)
    def setUp(self):
        TestUtilsPentagon.count += 1
        print("Enter n value as 4 and choose inifinte series - 2  ")
        self.pen1 = TestUtilsPentagon.pen1
        self.pen2 = TestUtilsPentagon.pen2
        self.pen2 = TestUtilsPentagon.pen3
        self.pen2 = TestUtilsPentagon.pen4
        self.pen2 = TestUtilsPentagon.pen5
        print("TESTCASE: " + str(TestUtilsPentagon.count) + " executing ...")
        self.get_mean()
        self.get_median()

    def get_mean(self):
        try:
            self.pen1.Mean()
            self.pen2.Mean()
            self.pen3.Mean()
            self.pen4.Mean()
            self.pen5.Mean()
            self.mean = self.pen1.avg1
        except AttributeError:
            print("Attribute error")
            self.mean = 11.0

    def get_median(self):
        try:
            self.pen1.Median()
            self.pen2.Median()
            self.pen3.Median()
            self.pen4.Median()
            self.pen5.Median()
            self.median = self.pen1.Median1
        except AttributeError:
            print("Attribute error")
            self.median = 9

    def test_is_Pentagon_series(self):
        self.assertIsInstance(self.pen1.series, list)
        for value in self.pen1.series:
            self.assertNotIsInstance(value, str)
            self.assertIsInstance(value, int)
        if self.pen2.lower_bound == 5 and self.pen2.upper_bound == 10: self.assertEqual(len(self.pen2.series), 6)
        self.assertIn(len(self.pen3.series), [5, 6, 10, 4])
        self.assertNotEqual(len(self.pen4.series), 0)
        TestUtilsPentagon.series = self.pen1.series

    def test_mean(self):
        self.get_mean()
        sum_of_series = sum(self.pen1.series)
        n = len(self.pen1.series)
        avg = sum_of_series / n
        self.assertEqual(self.pen1.avg, round(avg, 2))
        self.assertNotEqual(self.pen1.avg, 13.5)
        self.assertEqual(self.pen1.avg, 15.0)
        self.assertEqual(self.pen2.avg, 455.0)
        self.assertEqual(self.pen3.avg, 85.0)
        self.assertEqual(self.pen4.avg, 55.0)
        self.assertEqual(self.pen5.avg, 455.0)

        TestUtilsPentagon.mean = self.pen1.avg

    def test_median(self):
        self.get_median()
        n = len(self.series)
        self.assertEqual(self.pen1.median, 12)
        self.assertEqual(self.pen2.median, 451.0)
        self.assertEqual(self.pen3.median, 81.0)
        self.assertEqual(self.pen4.median, 43.0)
        self.assertEqual(self.pen5.median, 451.0)
        TestUtilsPentagon.median = self.pen1.median

    def tearDown(self):
        print("TESTCASE: " + str(TestUtilsPentagon.count) + " completed")

    @classmethod
    def tearDownClass(cls):
        print("-" * 100)
        print("\t\tSERIES:", cls.series, "\n\t\tMEDIAN:", cls.pen1.median, "\n\t\tMEAN:", cls.pen1.avg)
        print("\t\tLOWER:", cls.pen1.lower_bound, "\n\t\tUPPER:", cls.pen1.upper_bound, "\n\t\tCOUNT:",
              len(cls.pen1.series))
        print("-" * 100)
        print("\t\tEND OF Pentagon SERIES TEST SCENARIO")
        print("-" * 100)


#if __name__ == '__main__':
    #unittest.main(verbosity=3, argv=['first-arg-is-ignored'], exit=False)



