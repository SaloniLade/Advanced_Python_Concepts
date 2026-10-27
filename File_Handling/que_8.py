#Write a program to read a text file and display its lines in reverse order. 
with open("student.txt", "r") as file:
    lines = file.readlines()

print("Lines in reverse order:")

for line in reversed(lines):
    print(line.strip())