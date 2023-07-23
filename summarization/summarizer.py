# summarization/summarizer.py
# Interface for the summarization process

from .sumy_summarizer import SumySummarizer  # Import the SumySummarizer class
from .textblob_summarizer import TextBlobSummarizer  # Import the TextBlobSummarizer class
from .utils import clean_text

class Summarizer:
    def __init__(self, method='sumy'):
        # Initialize the selected summarization method
        self.method = method.lower()
        if self.method == 'sumy':
            self.summarizer = SumySummarizer()
        elif self.method == 'textblob':
            self.summarizer = TextBlobSummarizer()
        else:
            raise ValueError(f"Invalid summarization method: {method}. Choose 'sumy' or 'textblob'.")

    def generate_summary(self, text, length=5, focus='sentences'):
        # Clean the input text
        cleaned_text = clean_text(text)

        # Generate summary using the selected method
        summary = self.summarizer.generate_summary(cleaned_text, length, focus)

        return summary
