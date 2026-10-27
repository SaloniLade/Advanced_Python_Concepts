# Calculate percentage and grade for five subjects.
def calculate_grade(marks):
    percentage = sum(marks) / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    return percentage, grade

marks = []

for i in range(5):
    m = float(input("Enter subject marks: "))
    marks.append(m)

percentage, grade = calculate_grade(marks)

print("Percentage =", percentage, "%")
print("Grade =", grade)