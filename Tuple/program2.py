# Write a program to develope a system that manages the positions of points in a 2D plane. The position of each point is represented as a tuple of two values: (x, y). Write a program that:
# - Takes a list of points as input.
# - Calculates the distance between two given points.
# - Finds the point that is farthest from the origin (0, 0).
# Tasks:
# - Use tuples to represent the coordinates of each point.
# - Implement a function to calculate the Euclidean distance between two points using their tuple representations.
# - Implement a function to find the farthest point from the origin.

import math


def distance(point1, point2):
    return math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2
    )


def farthest_point(points):
    return max(
        points,
        key=lambda point: math.sqrt(point[0] ** 2 + point[1] ** 2)
    )


points = [(2, 3), (5, 6), (1, 1)]

print("Distance:", distance(points[0], points[1]))
print("Farthest Point:", farthest_point(points))