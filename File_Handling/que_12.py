#Read a text file and count how many times each word occurs. Display the result using a dictionary. 
with open("student.txt", "r") as file:
    content = file.read()

words = content.lower().split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count)