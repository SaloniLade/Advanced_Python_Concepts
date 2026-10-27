#  Create the following directory structure:
# a) college_project/ 
# b) main.py 
# c) student/ 
# d) __init__.py
# e) details.py 
# f) marks.py
# g) faculty/
# h) __init__.py 
# i) details.py 
# Write a program that imports functions from both packages and displays student and faculty information. 


from student.details import get_student_details
from student.marks import calculate_total, calculate_percentage
from faculty.details import get_faculty_details

student = get_student_details()
faculty = get_faculty_details()

marks = [85, 90, 80, 75, 70]

print("--- Student Information ---")
print("Name:", student["name"])
print("Roll Number:", student["roll_no"])
print("Course:", student["course"])
print("Total Marks:", calculate_total(marks))
print("Percentage:", calculate_percentage(marks), "%")

print("\n--- Faculty Information ---")
print("Name:", faculty["name"])
print("Department:", faculty["department"])
print("Subject:", faculty["subject"])
