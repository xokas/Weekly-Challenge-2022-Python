import unittest
 # https://realpython.com/python-testing/#unit-tests-vs-integration-tests

from Challenge3 import isPrime, createPrime

class Challenge3_test(unittest.TestCase):
    

    def test_zero(self):
        self.assertFalse(isPrime(0), "Bad result")

    def test_one(self):
        self.assertFalse(isPrime(1), "Bad result")

    def test_two(self):
        self.assertTrue(isPrime(2), "Bad result")

    def test_eleven(self):
        self.assertTrue(isPrime(11), "Bad result")

    def test_twelve(self):
        self.assertFalse(isPrime(12), "Bad result")

    def test_primes_below_hundred(self):
        self.assertEqual(len(createPrime(100)), 25, "Bad result")

   
if __name__ == "__main__":
    unittest.main()
    print("Everything passed")