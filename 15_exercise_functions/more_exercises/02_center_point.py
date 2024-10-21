import math


def distance_center(curr_x, curr_y):
    return math.sqrt(curr_x ** 2 + curr_y ** 2)


def closest_point(curr_x1, curr_y1, curr_x2, curr_y2):
    distance_1 = distance_center(curr_x1, curr_y1)
    distance_2 = distance_center(curr_x2, curr_y2)
    if distance_1 <= distance_2:
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(closest_point(x1, y1, x2, y2))
