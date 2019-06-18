# python -m unittest discover
import unittest
from knock71 import is_stopword


class TestKnockChp8(unittest.TestCase):
    def test_is_stopword(self):

        self.assertEqual(is_stopword('is'), True)
        self.assertEqual(is_stopword('me'), False)


if __name__ == '__main__':
    unittest.main()

# python -m unittest test_chapter8.py
