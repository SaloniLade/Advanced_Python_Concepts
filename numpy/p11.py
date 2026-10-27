# 11.Create a NumPy array containing numbers from 1 to 20. Using slicing, display:
# •	First 5 elements 
# •	Last 5 elements 
# •	Alternate elements 
# •	Elements in reverse order

import numpy as np

arr = np.arange(1, 21)

print("Original Array:", arr)

# Example slicing operations
print("First 5 Elements:", arr[:5])
print("Elements from Index 5 to 10:", arr[5:10])
print("Last 5 Elements:", arr[-5:])
print("Every Second Element:", arr[::2])