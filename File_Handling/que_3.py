#Write a program to append additional student information to an existing file without deleting its previous contents. 

info = input("Enter additional information: ")

with open("student.txt", "a") as file:
    file.write(info + "\n")

print("Information appended successfully.")