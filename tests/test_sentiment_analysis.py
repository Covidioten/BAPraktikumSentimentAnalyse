
# -*- coding: utf-8 -*-

from .context import sentiment_analysis

import unittest


class BasicTestSuite(unittest.TestCase):
    """Test polarity of sentence"""

    def test_sentence_with_positive_sentiment(self):
        self.assertGreater(sentiment_analysis.get_sentiment_of_string(
            "Der Lockdown ist gut"), 0)
        
    def test_sentence_with_negative_sentiment(self):
        self.assertLess(sentiment_analysis.get_sentiment_of_string(
        "Der Lockdown ist nicht gut"), 0)
        
    def test_sentence_with_negative_sentiment(self):
        self.assertEqual(sentiment_analysis.get_sentiment_of_string(
        "Der Himmel ist blau"), 0)


if __name__ == '__main__':
    unittest.main()
