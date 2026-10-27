# Write a program to build a keyword extraction tool for summarizing research papers. The program should:
# - Accept a block of text as input.
# - Extract keywords from the text based on word frequency or term importance (e.g., TF-IDF).
# - Return a list of the top 5 keywords.
# Tasks:
# - Use simple frequency analysis or implement TF-IDF (Term Frequency-Inverse Document Frequency) for extracting important words.
# - Remove stopwords and irrelevant words before extracting keywords.


import re
from collections import Counter

text = input("Enter text: ")

stopwords = {
    "is", "the", "a", "an", "and", "to", "in",
    "of", "are", "was", "for", "it", "on", "with"
}

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

keywords = [
    word for word in words
    if word not in stopwords
]

frequency = Counter(keywords)

print("\nTop 5 Keywords:")
for word, count in frequency.most_common(5):
    print(word, ":", count)
