import unittest

from nltk.corpus import stopwords


class StopWord:
    def __init__(self):
        self.stopword_set = set(stopwords.words('english'))

    def check(self, word: str) -> bool:
        return word in self.stopword_set


class TestStopWord(unittest.TestCase):
    def test_stopword(self):
        stopword = StopWord()
        test_set = [('a', True), ('e', False)]
        # test_set = [('a', False), ('e', False), ('e', True)]

        for word, expected_result in test_set:
            with self.subTest(word=word):
                result = stopword.check(word)
                self.assertEqual(result, expected_result)


def main():
    stopword = StopWord()
    print(stopword.stopword_set)

    unittest.main()


if __name__ == '__main__':
    main()
