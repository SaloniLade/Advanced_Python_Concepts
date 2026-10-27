# Write a program that counts the frequency of each character in a given string. The program should:
# - Count how many times each character (including spaces and punctuation) appears in the string.
# - Display the frequency of each character in descending order of frequency.
# - Allow the user to ignore case or make it case-sensitive.
# Tasks:
# - Use a dictionary to store the frequency of each character.
# - Sort the dictionary by frequency in descending order.




text = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

sorted_frequency = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

for char, count in sorted_frequency:
    print(char, ":", count)