# 10. Create a package texttools containing: 
# a) cleaning.py – remove punctuation and extra spaces 
# b) tokenization.py – tokenize text 
# c) frequency.py – word-frequency analysis 
# Create a main program to use the package. 
from texttools.cleaning import clean_text
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = input("Enter a sentence: ")

cleaned = clean_text(text)
tokens = tokenize(cleaned)
frequency = word_frequency(tokens)

print("\n--- Text Analysis ---")
print("Original Text:", text)
print("Cleaned Text:", cleaned)
print("Tokens:", tokens)
print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count)
