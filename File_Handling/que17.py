# Create a file containing student records in the format: RollNo,Name,Marks 
# 101,Amit,85 
# 102,Priya,92 
# 103,Rahul,78 
# Write a program to: 
# • Display all records.
# • Find the student with the highest marks. 
# • Calculate average marks. 
# • Display students who scored more than 80. 
# Create a file containing student records
with open("students.txt", "w") as file:
    file.write("101,Amit,85\n")
    file.write("102,Priya,92\n")
    file.write("103,Rahul,78\n")

students = []


with open("students.txt", "r") as file:
    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append((roll, name, int(marks)))


print("All Student Records:")
for student in students:
    print(student)


topper = max(students, key=lambda s: s[2])
print("\nHighest Marks:", topper[1], topper[2])


average = sum(s[2] for s in students) / len(students)
print("Average Marks:", average)


print("\nStudents scoring above 80:")
for s in students:
    if s[2] > 80:
        print(s[1], s[2])