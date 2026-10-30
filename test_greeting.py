import unittest

from greeting import get_greeting


class TestGreeting(unittest.TestCase):

    def test_morning(self):
        self.assertEqual(get_greeting(8), "Good Morning Sir")

    def test_afternoon(self):
        self.assertEqual(get_greeting(14), "Good Afternoon Sir")

    def test_evening(self):
        self.assertEqual(get_greeting(18), "Good Evening Sir")

    def test_night(self):
        self.assertEqual(get_greeting(22), "Good Night Sir")

    def test_midnight(self):
        self.assertEqual(get_greeting(0), "Good Morning Sir")

    def test_invalid_hour(self):
        with self.assertRaises(ValueError):
            get_greeting(24)


if __name__ == "__main__":
    unittest.main()
