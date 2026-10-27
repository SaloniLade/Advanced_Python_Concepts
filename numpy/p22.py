# 22.	Generate a random 3D array of shape (3, 4, 5) and calculate its:
# •	Mean
# •	Median
# •	Standard Deviation
# •	Variance
# •	Minimum
# •	Maximum

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array:")
print(arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))