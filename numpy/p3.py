# 3.	Create a NumPy array containing 10 numbers. Find and display the maximum, minimum, sum, and average of the elements.
import numpy as np

arr = np.array([12, 25, 8, 40, 15, 30, 5, 18, 35, 22])

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))