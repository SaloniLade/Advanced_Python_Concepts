#Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file. 
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    content = file.read()

modified_content = content.replace(old_word, new_word)

with open("student_new.txt", "w") as file:
    file.write(modified_content)

print("Word replaced successfully.")
print("Modified file saved as student_new.txt")