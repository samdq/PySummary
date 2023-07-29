# tests/test_summarizer.py
# Unit tests for the Summarizer class

import unittest
from summarization.summarizer import Summarizer

class TestSummarizer(unittest.TestCase):
    def test_sumy_summarization(self):
        summarizer = Summarizer(method='sumy')
        summary = summarizer.generate_summary("Test summarization with Sumy.", length=2, focus='sentences')
        self.assertTrue(len(summary) > 0)

    def test_textblob_summarization(self):
        summarizer = Summarizer(method='textblob')
        summary = summarizer.generate_summary("Test summarization with TextBlob.", length=3, focus='words')
        self.assertTrue(len(summary) > 0)

if __name__ == '__main__':
    unittest.main()
