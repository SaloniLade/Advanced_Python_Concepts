# 15.	Create two NumPy arrays and concatenate them horizontally and vertically. 
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

print("Horizontal Concatenation:")
print(np.hstack((a, b)))

print("Vertical Concatenation:")
print(np.vstack((a, b)))