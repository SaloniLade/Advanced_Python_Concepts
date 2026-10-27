
with open("file1.txt", "r") as f1:
    text1 = f1.read()

with open("file2.txt", "r") as f2:
    text2 = f2.read()

with open("file3.txt", "w") as f3:
    f3.write(text1)
    f3.write("\n")
    f3.write(text2)

print("Files combined successfully!")

with open("file3.txt", "r") as f3:
    print(f3.read())
