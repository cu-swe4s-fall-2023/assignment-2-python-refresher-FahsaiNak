import sys

sys.path.insert(0, '../../src')

# Import necessary modules and libraries
import my_utils
import unittest
import random
import os
import numpy as np

# Create a test class for testing calculation functions
class TestCalc(unittest.TestCase):
    def setUp(self):
        # Generate a random list for testing
        self.lst_test = list(random.sample(range(-100, 100), random.randint(1, 20)))
        # Calculate the expected mean, median, and standard deviation using numpy
        self.direct_mean = round(np.mean(self.lst_test), 2)
        self.direct_median = round(np.median(self.lst_test), 2)
        self.direct_std = round(np.std(self.lst_test), 2)

    def test_calculate_mean(self):
        # Test the calculate_mean function
        mean = my_utils.calculate_mean(self.lst_test)
        self.assertEqual(mean, self.direct_mean)  # Check if the calculated mean matches the expected mean
        self.assertRaises(ZeroDivisionError, my_utils.calculate_mean, list())  # Test with an empty list
        self.assertRaises(TypeError, my_utils.calculate_mean, None)  # Test with None as input

    def test_calculate_median(self):
        # Test the calculate_median function
        median = my_utils.calculate_median(self.lst_test)
        self.assertEqual(median, self.direct_median)  # Check if the calculated median matches the expected median
        self.assertRaises(IndexError, my_utils.calculate_median, list())  # Test with an empty list
        self.assertRaises(TypeError, my_utils.calculate_median, None)  # Test with None as input

    def test_calculate_std_dev(self):
        # Test the calculate_std_dev function
        std = my_utils.calculate_std_dev(self.lst_test)
        self.assertEqual(std, self.direct_std)  # Check if the calculated std_dev matches the expected std_dev
        self.assertRaises(ZeroDivisionError, my_utils.calculate_std_dev, list())  # Test with an empty list
        self.assertRaises(TypeError, my_utils.calculate_median, None)  # Test with None as input

# Create a test class for testing get_column function
class TestGetCol(unittest.TestCase):
    def setUp(self):
        # Generate a test file with random data for get_column testing
        self.test_file_name = 'setup_test_file.txt'
        num_col = random.randint(1, 100)
        self.query_column = random.randint(1, num_col)
        self.query_value = str(random.randint(-10, 10))
        self.result_column = random.randint(1, num_col)
        self.lst_column = list()

        f = open(self.test_file_name, 'w')
        for n in range(100):
            for i in range(num_col):
                val = random.randint(-10, 10)
                if n % 3 == 0:
                    if i == self.query_column - 1:
                        val = int(self.query_value)
                    if i == self.result_column - 1:
                        self.lst_column.append(val)
                else:
                    val = int(self.query_value) + random.randint(1, 10)
                f.write(str(val))
                if i == num_col - 1:
                    f.write('\n')
                else:
                    f.write(',')
        f.close()

    def tearDown(self):
        # Remove the test file after testing
        os.remove(self.test_file_name)

    def test_get_column(self):
        # Test the get_column function
        lst = my_utils.get_column(self.test_file_name, self.query_column,
                                  self.query_value, result_column=self.result_column)
        self.assertEqual(lst, self.lst_column)  # Check if the extracted column matches the expected result

if __name__ == '__main__':
    unittest.main()