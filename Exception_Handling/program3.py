# IndexError exception

try:
    a = [10, 20, 30]
    print(a[5])

except IndexError:
    print("List index is out of range")