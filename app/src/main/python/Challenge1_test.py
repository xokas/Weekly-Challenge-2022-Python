import unittest
 # https://realpython.com/python-testing/#unit-tests-vs-integration-tests

from Challenge1 import check_anagram


class Challenge1_test(unittest.TestCase):
    def test_two_words_equals(self):
        self.assertFalse(check_anagram("first", "first"), "Equal words are not anagrams")

    def test_two_words_differents(self):
        self.assertFalse(check_anagram("first", "second"), "Different words are not anagrams")

    def test_two_words_with_same_letters(self):
        self.assertFalse(check_anagram("first", "ffiirrsstt"), "One word contains letters from other word")

    def test_two_anagrams(self):
        self.assertTrue(check_anagram("first", "tsrif"))

    def test_two_anagrams_with_upper_case_letters(self):
        self.assertTrue(check_anagram("fiRSt", "TsrIf"))

   
if __name__ == "__main__":
    unittest.main()
    print("Everything passed")