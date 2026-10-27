# 8. Create a package student containing: 
# a) marks.py – total and percentage 
# b) grade.py – grade calculation  
# c) attendance.py – attendance eligibility 
# Write a main program that uses all three modules to generate a student report. 
from student.marks import total_marks, percentage
from student.grade import calculate_grade
from student.attendance import attendance_eligibility

name = input("Enter student name: ")

marks = list(map(float, input(
    "Enter marks in 5 subjects (out of 100): "
).split()))

if len(marks) != 5 or any(m < 0 or m > 100 for m in marks):
    print("Please enter exactly 5 valid marks between 0 and 100.")
else:
    attended = int(input("Classes attended: "))
    total_classes = int(input("Total classes: "))

    total = total_marks(marks)
    percent = percentage(marks)
    grade = calculate_grade(percent)
    attendance = attendance_eligibility(
        attended, total_classes
    )

    print("\n--- Student Report ---")
    print("Name:", name)
    print("Total Marks:", total, "/ 500")
    print("Percentage:", round(percent, 2), "%")
    print("Grade:", grade)
    print("Attendance:", attendance)
