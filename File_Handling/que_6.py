#Write a program to count the total number of words present in a text file. 
with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total number of words:", len(words))