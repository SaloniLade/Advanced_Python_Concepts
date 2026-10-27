#Read a text file and find the longest word present in the file. 
with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

longest_word = max(words, key=len)

print("Longest word:", longest_word)
print("Length:", len(longest_word))