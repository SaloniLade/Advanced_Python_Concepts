# 12.	Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy Boolean indexing.
import numpy as np

arr = np.array([10, 25, 60, 45, 75, 30, 90, 50, 65, 20])

arr[arr > 50] = 0

print("Updated Array:", arr)