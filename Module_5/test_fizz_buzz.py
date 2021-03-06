import unittest
import fizz_buzz


class FizzBuzzTestCase(unittest.TestCase):
    def test_fizz(self):
        number = 6
        result = fizz_buzz.get_reply(number)
        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        number = 5
        result = fizz_buzz.get_reply(number)
        self.assertEqual(result, 'Buzz')

    def test_fizz_buzz(self):
        number = 15
        result = fizz_buzz.get_reply(number)
        self.assertEqual(result, "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
