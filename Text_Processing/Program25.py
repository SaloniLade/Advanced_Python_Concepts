# Write a program to develop a tool that summarizes long pieces of text. Write a program that:
# - Accepts a block of text as input.
# - Identifies the most important sentences in the text by analyzing keywords or frequency of words.
# - Returns a short summary by selecting the most relevant sentences.
# Tasks:
# - Implement text ranking techniques based on frequency or keyword analysis.
# - Extract and return key sentences to form the summary.


import re
from collections import Counter

text = input("Enter a paragraph: ")

sentences = re.split(r'(?<=[.!?])\s+', text.strip())

stopwords = {
    "is", "the", "a", "an", "and", "to", "of",
    "in", "are", "was", "for", "it", "this"
}

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
words = [word for word in words if word not in stopwords]

frequency = Counter(words)
scores = []

for sentence in sentences:
    sentence_words = re.findall(
        r'\b[a-zA-Z]+\b', sentence.lower()
    )
    score = sum(frequency[word] for word in sentence_words)
    scores.append((score, sentence))

top_sentences = sorted(scores, reverse=True)[:2]

print("\nSummary:")
for score, sentence in sorted(
    top_sentences, key=lambda item: sentences.index(item[1])
):
    print(sentence)
