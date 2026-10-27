#Write a program to read a text file line by line and display each line separately.
with open("student.txt", "r") as file:

    for line in file:
        print(line.strip())