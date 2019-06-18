# python -m unittest discover
import unittest
from knock71 import is_stopword, stopwords


class TestKnockChp8(unittest.TestCase):
    def test_is_stopword(self):

        self.assertEqual(is_stopword('is', stopwords), True)
        self.assertEqual(is_stopword('me', stopwords), False)


if __name__ == '__main__':
    unittest.main()
