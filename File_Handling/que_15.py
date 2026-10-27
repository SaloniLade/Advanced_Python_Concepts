#Read a Python source file and create another file after removing single-line comments.
with open("program.py", "r") as file:
    lines = file.readlines()

with open("program_without_comments.py", "w") as file:

    for line in lines:

        if not line.strip().startswith("#"):
            file.write(line)

print("Comments removed successfully.")
print("New file: program_without_comments.py")