# 25.	Create a 3D array of random integers between 1 and 100. Flatten the array and perform the following operations:
# •	Display elements greater than 50
# •	Display even numbers
# •	Display elements less than the average

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

flat = arr.flatten()
avg = np.mean(flat)

print("Original 3D Array:")
print(arr)

print("Flattened Array:")
print(flat)

print("Elements Greater Than 50:")
print(flat[flat > 50])

print("Even Numbers:")
print(flat[flat % 2 == 0])

print("Elements Less Than Average:")
print(flat[flat < avg])

print("Average:", avg)