# 17.	Take marks of 20 students, calculate the class average and display the marks of students who scored above the average.
import numpy as np

marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 82,
                  55, 72, 68, 92, 78, 84, 50, 89, 76, 81])

average = np.mean(marks)

print("Student Marks:", marks)
print("Class Average:", average)
print("Marks Above Average:", marks[marks > average])