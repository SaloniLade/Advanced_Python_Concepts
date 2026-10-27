# Write a program to build a tool for cleaning text data, and you need to remove common stopwords (e.g., "is", "and", "the") from a given paragraph. Write a program that:
# - Accepts a block of text as input.
# - Removes all common stopwords from the text.
# - Returns the cleaned version of the text.
# Tasks:
# - Use a predefined list of stopwords or import a stopword list from libraries like nltk.
# - Process the text by removing stopwords and ensuring proper spacing and punctuation.


text = input("Enter a sentence: ")

stopwords = {
    "is", "the", "a", "an", "and", "to",
    "in", "of", "are", "was", "for", "on"
}

words = text.split()

filtered_words = [
    word for word in words
    if word.lower().strip(".,!?") not in stopwords
]

result = " ".join(filtered_words)

print("Original text:", text)
print("Text after removing stopwords:", result)
