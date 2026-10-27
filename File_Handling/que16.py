#  Read a text file and create another file containing the same text in uppercase.
          
with open("input.txt", "r") as file:
    text = file.read()


with open("uppercase.txt", "w") as file:
    file.write(text.upper())

print("Text copied in uppercase successfully!")

