#Read a text file and count the number of vowels and consonants present in the file. 

with open("student.txt", "r") as file:
    content = file.read()

vowels = 0
consonants = 0

for ch in content.lower():

    if ch in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
