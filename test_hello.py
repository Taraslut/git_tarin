import unittest

from .example import hello


class MyTestCase(unittest.TestCase):
    def test_something(self):
        rez1 = hello("")
        self.assertEqual(rez1, "hello ")

    def test_name(self):
        rez2 = hello('Taras')
        self.assertEqual(rez2, "hello Taras")


if __name__ == '__main__':
    unittest.main()
