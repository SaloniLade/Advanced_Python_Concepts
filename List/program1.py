# Write a program to building a simple student grade management system for a class of students. The system will store student names and their grades (both as lists) and should be able to perform the following operations:
# Add a new student and their grade.
# Update the grade of an existing student.
# Remove a student from the list.
# Calculate and display the average grade of the class.
# Display the highest and lowest grades in the class.
# Tasks:
# Use lists to store the student names and their corresponding grades.
# Implement functions to add, update, remove, and calculate the average and extreme grades.

students = []
grades = []


def add_student(name, grade):
    students.append(name)
    grades.append(grade)


def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print("Grade updated successfully")
    else:
        print("Student not found")


def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully")
    else:
        print("Student not found")


def display_details():
    print("\nStudent Details:")
    for i in range(len(students)):
        print(students[i], "-", grades[i])


def calculate_details():
    if grades:
        print("Average:", sum(grades) / len(grades))
        print("Highest Grade:", max(grades))
        print("Lowest Grade:", min(grades))


add_student("Saloni", 85)
add_student("Rahul", 90)
add_student("Priya", 78)

display_details()
calculate_details()