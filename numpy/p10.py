# 10.	Create a 4 × 4 matrix and calculate the sum of each row and each column separately.
import numpy as np

arr = np.array([[1,  2,  3,  4],
                [5,  6,  7,  8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Matrix:\n", arr)
print("Sum of Each Row:", np.sum(arr, axis=1))
print("Sum of Each Column:", np.sum(arr, axis=0))