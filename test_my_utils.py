import my_utils
import unittest
import random
import numpy as np


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.lst_test = list(random.sample(range(-100, 100), 5))
        self.direct_mean = np.mean(self.lst_test)
        self.direct_median = np.median(self.lst_test)
        self.direct_std = np.std(self.lst_test)

    def test_calculate_mean(self):
        mean = my_utils.calculate_mean(self.lst_test)
        self.assertEqual(mean, self.direct_mean)
        self.assertRaises(TypeError, my_utils.calculate_mean, None)

    def test_calculate_median(self):
        median = my_utils.calculate_median(self.lst_test)
        self.assertEqual(median, self.direct_median)
        self.assertRaises(TypeError, my_utils.calculate_median, None)

    def test_calculate_std_dev(self):
        std = my_utils.calculate_std_dev(self.lst_test)
        self.assertEqual(std, self.direct_std)
        self.assertRaises(TypeError, my_utils.calculate_median, None)


if __name__ == '__main__':
    unittest.main()
