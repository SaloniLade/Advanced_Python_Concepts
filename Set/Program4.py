# Write a program to manage two different projects in your company, and you need to analyze employee involvement. The employees working on each project are represented as sets. Write a program that:
# - Displays the employees working on both projects (intersection).
# - Displays the employees working only on one project (difference).
# - Displays the total unique employees across both projects (union).
# Tasks:
# - Use sets to represent the employees in each project.
# - Perform union, intersection, and difference operations to analyze employee involvement.

project_a = {"Saloni", "Rahul", "Priya"}
project_b = {"Rahul", "Amit", "Priya"}

print("Common Employees:", project_a & project_b)
print("Only in Project A:", project_a - project_b)
print("Only in Project B:", project_b - project_a)
print("All Unique Employees:", project_a | project_b)