# 13.	Create an unsorted NumPy array and display it in:
# •	Ascending order 
# •	Descending order

import numpy as np

arr = np.array([45, 12, 78, 23, 56, 9])

print("Original Array:", arr)
print("Ascending Order:", np.sort(arr))
print("Descending Order:", np.sort(arr)[::-1])