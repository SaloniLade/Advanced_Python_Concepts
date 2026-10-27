# Create a module student.py containing functions to calculate total marks, percentage, and grade. 
# Import the module into another Python program and generate a student's result.
import student

name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = student.total_marks(marks)
percent = student.percentage(marks)
result_grade = student.grade(percent)

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percent, 2), "%")
print("Grade:", result_grade)
