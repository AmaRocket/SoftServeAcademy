import unittest
import count_vowels

class CountTest(unittest.TestCase):
    def test_get_res(self):
        self.assertEqual(count_vowels.get_res("aaabbbccc"), 3)

    def test_get_res_1(self):
        self.assertEqual(count_vowels.get_res("AAAYYYUUUGGGEEEHHHLLLooo"), 15)

if __name__ == '__main__':
    unittest.main()