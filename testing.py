# doctest: doctest is a module that allows you to test your code by running examples embedded in the documentation and verifying that they produce the expected results.
from unittest.mock import Mock
import unittest
import mymath
import doctest


def add(a, b):
    """
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    """
    return a+b


doctest.testmod()

# unittest: unittest is a module that allows you to write test cases for your code.
# The unittest module provides a rich set of tools for constructing and running tests.
# This section demonstrates that a small subset of the tools suffice to meet the needs of most users.
# Here is a short example of how to write a test case:
# test methods: A test method is a method whose name starts with test, which the unittest module would try to run.
# command to run the test: python -m unittest module_name
# Example to run this test: python -m unittest testing
# unittest module provides a setup and teardown feature to initialize and clean up the test environment that will be used while executing each test cases.


class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def setUp(self) -> None:
        return super().setUp()

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    # This is how you skip a test
    @unittest.skip('Skip this test')
    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def tearDown(self) -> None:
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()

# Mocking: Self explanatory


class TestClass():
    pass


cls = TestClass()
cls.method = Mock(return_value='mocking is fun')
cls.method(1, 2, 3)
# 'mocking is fun'

cls.method.assert_called_once_with(1, 2, 3)
cls.method(1, 2, 3)
# 'mocking is fun'

cls.method.assert_called_once_with(1, 2, 3)
# Traceback (most recent call last):
# File "/usercode/__ed_file.py", line 14, in <module>
# cls.method.assert_called_once_with(1, 2, 3)
# File "/usr/lib/python3.5/unittest/mock.py", line 804, in assert_called_once_with
# raise AssertionError(msg)
# AssertionError: Expected 'mock' to be called once. Called 2 times.

cls.other_method = Mock(return_value='Something else')
cls.other_method.assert_not_called()

# test coverage: coverage.py is a tool for measuring code coverage of Python programs.
# pip3 install coverage
# coverage run testing.py
# coverage report -m
# coverage html
