#Write a program to count and display the total number of lines present in a text file. 

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))