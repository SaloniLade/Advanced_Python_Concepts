# FileNotFoundError exception

try:
    f = open("abc.txt", "r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File not found")