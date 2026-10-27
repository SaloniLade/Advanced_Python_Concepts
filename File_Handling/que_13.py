#Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears. 

word = input("Enter word to search: ")

count = 0

with open("student.txt", "r") as file:

    for line_number, line in enumerate(file, start=1):

        words = line.split()

        for w in words:

            if w.lower() == word.lower():
                count += 1
                print("Found at line:", line_number)

print("Total occurrences:", count)