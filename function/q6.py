# Calculate the area of a circle using its radius.
# Formula: Area = π × r × r
def area_circle(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))
print("Area of circle =", area_circle(r))