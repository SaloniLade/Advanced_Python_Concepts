# Write a program to develop an attendance system for a classroom. The system should track students who attended classes over a week. You need to:
# - Store the names of students who attended class each day in a dictionary, where the day of the week is the key and the set of students is the value.
# - Identify students who attended all classes during the week.
# - Identify students who attended only one class during the week.
# - Count the total number of unique students who attended at least one class during the week.
# Tasks:
# - Use a dictionary where the keys are days of the week, and the values are sets of students.
# - Use set operations to find students who attended all or only one class.

attendance = {
    "Monday": {"Saloni", "Rahul", "Amit"},
    "Tuesday": {"Saloni", "Priya"},
    "Wednesday": {"Saloni", "Rahul"},
    "Thursday": {"Saloni", "Amit"},
    "Friday": {"Saloni", "Priya"}
}

all_days = list(attendance.values())

all_attended = set.intersection(*all_days)
unique_students = set.union(*all_days)

one_day_students = set()

for student in unique_students:
    count = sum(student in day for day in all_days)

    if count == 1:
        one_day_students.add(student)

print("Attended all days:", all_attended)
print("Attended only one day:", one_day_students)
print("Total unique students:", len(unique_students))