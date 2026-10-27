#  Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.
 
with open("attendance.txt", "w") as file:
    file.write("Amit,18,20\n")
    file.write("Priya,14,20\n")
    file.write("Rahul,12,20\n")

print("Attendance Percentages:")
print("Students below 75% attendance:")

with open("attendance.txt", "r") as file:
    for line in file:
        name, attended, total = line.strip().split(",")

        attended = int(attended)
        total = int(total)

        if total == 0:
            percentage = 0
        else:
            percentage = (attended / total) * 100

        print(name, ":", percentage, "%")

        if percentage < 75:
            print(name, "has attendance below 75%")