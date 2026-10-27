# 16.	Store marks of 10 students in a NumPy array. Calculate:
# •	Highest marks 
# •	Lowest marks 
# •	Average marks 
# •	Median 
# •	Standard deviation


import numpy as np

marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 82])

print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Standard Deviation:", np.std(marks))