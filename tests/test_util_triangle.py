from NumberGenerator.Sequences.Triangle import Triangle
import unittest
import numpy as np


class TestUtilsTriangle(unittest.TestCase):
    series = []
    count = 0

    @classmethod
    def setUpClass(cls):
        print("-" * 100)
        print("\t\tSTART Triangle SERIES TEST SCENARIO")
        print("-" * 100)
        if len(cls.series) == 0:
            print("Enter n values as 5")
            cls.tri1 = Triangle()
            print("Enter n value as 4 and choose inifinte series - 2 ")
            cls.tri2 = Triangle(query=2)
            cls.tri3 = Triangle(query=3, lower_bound=5, upper_bound=10)
            cls.tri4 = Triangle(query=3, lower_bound=1, upper_bound=10)
            cls.tri5 = Triangle(query=3, lower_bound=15, upper_bound=20)
    def setUp(self):
        TestUtilsTriangle.count += 1
        self.tri1 = TestUtilsTriangle.tri1
        self.tri2 = TestUtilsTriangle.tri2
        self.tri3 = TestUtilsTriangle.tri3
        self.tri4 = TestUtilsTriangle.tri4
        self.tri5 = TestUtilsTriangle.tri5
        print("TESTCASE: " + str(TestUtilsTriangle.count) + " executing ...")
        self.get_mean()
        self.get_median()

    def get_mean(self):
        try:
            self.tri1.Mean()
            self.tri2.Mean()
            self.tri3.Mean()
            self.tri4.Mean()
            self.tri5.Mean()
            self.mean = self.tri1.avg1
        except AttributeError:
            print("Attribute error")
            self.mean = 11.0

    def get_median(self):
        try:
            self.tri1.Median()
            self.tri2.Median()
            self.tri3.Median()
            self.tri4.Median()
            self.tri5.Median()
            self.median = self.tri1.Median1
        except AttributeError:
            print("Attribute error")
            self.median = 9

    def test_is_Triangle_series(self):
        self.assertIsInstance(self.tri1.series, list)
        for value in self.tri1.series:
            self.assertNotIsInstance(value, str)
            self.assertIsInstance(value, int)
        if self.tri2.lower_bound == 5 and self.tri2.upper_bound == 10: self.assertEqual(len(self.tri2.series), 6)
        self.assertIn(len(self.tri3.series), [5, 6, 10, 4])
        self.assertNotEqual(len(self.tri4.series), 0)
        TestUtilsTriangle.series = self.tri1.series

    def test_mean(self):
        self.get_mean()
        sum_of_series = sum(self.tri1.series)
        n = len(self.tri1.series)
        avg = sum_of_series / n
        self.assertEqual(self.tri1.avg, round(avg, 2))
        self.assertNotEqual(self.tri1.avg, 13.5)
        self.assertEqual(self.tri1.avg, 7.0)
        self.assertEqual(self.tri2.avg, 5.0)
        self.assertEqual(self.tri3.avg, 33.33)
        self.assertEqual(self.tri4.avg, 22.0)
        self.assertEqual(self.tri5.avg, 163.33)
        TestUtilsTriangle.mean = self.tri1.avg

    def test_median(self):
        self.get_median()
        n = len(self.series)
        self.assertEqual(self.tri1.median, 6)
        self.assertEqual(self.tri2.median, 4.5)
        self.assertEqual(self.tri3.median, 32.0)
        self.assertEqual(self.tri4.median, 18.0)
        self.assertEqual(self.tri5.median, 162.0)
        TestUtilsTriangle.median = self.tri1.median

    def tearDown(self):
        print("TESTCASE: " + str(TestUtilsTriangle.count) + " completed")

    @classmethod
    def tearDownClass(cls):
        print("-" * 100)
        print("\t\tSERIES:", cls.series, "\n\t\tMEDIAN:", cls.tri1.median, "\n\t\tMEAN:", cls.tri1.avg)
        print("\t\tLOWER:", cls.tri1.lower_bound, "\n\t\tUPPER:", cls.tri1.upper_bound, "\n\t\tCOUNT:",
              len(cls.tri1.series))
        print("-" * 100)
        print("\t\tEND OF Triangle SERIES TEST SCENARIO")
        print("-" * 100)


#if __name__ == '__main__':
    #unittest.main(verbosity=3, argv=['first-arg-is-ignored'], exit=False)



