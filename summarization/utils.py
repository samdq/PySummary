# summarization/utils.py
# Utility functions for text processing

import re

def clean_text(text):
    # Remove special characters, extra spaces, and newlines
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)
    cleaned_text = cleaned_text.strip()

    return cleaned_text
