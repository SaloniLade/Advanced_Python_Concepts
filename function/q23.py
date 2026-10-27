# Student records using separate functions
# Calculate total marks, percentage, grade, class average, highest scorer, and lowest scorer.
def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 60:
        return "C"
    elif p >= 40:
        return "D"
    else:
        return "Fail"

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = []

    for j in range(5):
        m = float(input("Enter subject marks: "))
        marks.append(m)

    students.append((name, roll, marks))

for s in students:
    p = percentage(s[2])
    print("\nName:", s[0])
    print("Roll No:", s[1])
    print("Total:", total_marks(s[2]))
    print("Percentage:", p)
    print("Grade:", grade(p))

percentages = [percentage(s[2]) for s in students]

if students:
    print("\nClass Average:", sum(percentages) / len(percentages))
    print("Highest Scorer:", students[percentages.index(max(percentages))][0])
    print("Lowest Scorer:", students[percentages.index(min(percentages))][0])