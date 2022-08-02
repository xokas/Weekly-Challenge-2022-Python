import unittest
 # https://realpython.com/python-testing/#unit-tests-vs-integration-tests

from Challenge2 import fibonacci
from random import seed
from random import randint


class Challenge2_test(unittest.TestCase):
    

    def test_first_element(self):
        self.assertEqual(fibonacci(1)[0], 0, "Bad result")

    def test_second_element(self):
        self.assertEqual(fibonacci(2)[1], 1, "Bad result")

    def test_third_element(self):
        self.assertEqual(fibonacci(3)[2], 1, "Bad result")

    def test_two_elements(self):
        list = fibonacci(50)
        seed(1)
        a = randint(0, 50)
        b = a + 1
        c = a + 2
        
        self.assertEqual(list[a] + list[b], list[c], "Bad result")

   
if __name__ == "__main__":
    unittest.main()
    print("Everything passed")