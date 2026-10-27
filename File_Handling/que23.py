# Write a program to compare two text files and display whether their contents are identical. 
# If different, identify the first line where they differ. 

with open("file1.txt", "r") as file1:
    lines1 = file1.readlines()

with open("file2.txt", "r") as file2:
    lines2 = file2.readlines()

identical = True
max_lines = max(len(lines1), len(lines2))

for i in range(max_lines):
    line1 = lines1[i] if i < len(lines1) else None
    line2 = lines2[i] if i < len(lines2) else None

    if line1 != line2:
        identical = False
        print("Files are different.")
        print("First difference at line:", i + 1)
        print("File 1:", repr(line1))
        print("File 2:", repr(line2))
        break

if identical:
    print("Both files are identical.")

    