# Write a program to build a simple text analysis tool. The tool should perform the following operations on a given paragraph of text:
# - Count the total number of words.
# - Count the frequency of each word.
# - Identify and display the top 3 most frequent words.
# - Count the number of vowels in the entire text.
# Tasks:
# - Use string manipulation to split the text into words and to check for vowels.
# - Use a dictionary to store the word frequencies.


text = input("Enter a paragraph: ")

words = text.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Total words:", len(words))

print("Word frequency:")
print(frequency)

top_words = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

print("Top 3 words:", top_words)

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)

print("Number of vowels:", vowel_count)