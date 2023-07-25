# summarization/sumy_summarizer.py
# Implementation of the summarization process using the Sumy library

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from .utils import clean_text

class SumySummarizer:
    def __init__(self):
        # Initialize SumySummarizer with necessary components
        self.tokenizer = Tokenizer('english')
        self.summarizer = LsaSummarizer()

    def generate_summary(self, text, length=5, focus='sentences'):
        # Clean the input text
        cleaned_text = clean_text(text)

        # Parse the cleaned text
        parser = PlaintextParser.from_string(cleaned_text, self.tokenizer)

        # Summarize based on the specified length and focus
        if focus == 'sentences':
            sentences = self.summarizer(parser.document, length)
            summary = ' '.join(str(sentence) for sentence in sentences)
        elif focus == 'words':
            words = self.summarizer(parser.document, length)
            summary = ' '.join(str(word) for word in words)
        else:
            raise ValueError(f"Invalid focus option: {focus}. Choose 'sentences' or 'words'.")

        return summary
