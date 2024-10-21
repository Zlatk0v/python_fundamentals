import math


def distance_to_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def line_length(def_x1, def_y1, def_x2, def_y2):
    return math.sqrt((def_x2 - def_x1) ** 2 + (def_y2 - def_y1) ** 2)


def closest_point(def_x1, def_y1, def_x2, def_y2):
    if distance_to_center(def_x1, def_y1) <= distance_to_center(def_x2, def_y2):
        return def_x1, def_y1, def_x2, def_y2
    else:
        return def_x2, def_y2, def_x1, def_y1


def print_longer_line(def_x1, def_y1, def_x2, def_y2, def_x3, def_y3, def_x4, def_y4):
    length_line1 = line_length(def_x1, def_y1, def_x2, def_y2)
    length_line2 = line_length(def_x3, def_y3, def_x4, def_y4)

    if length_line1 >= length_line2:
        closest_x1, closest_y1, farthest_x1, farthest_y1 = closest_point(def_x1, def_y1, def_x2, def_y2)
        print(
            f"({math.floor(closest_x1)}, {math.floor(closest_y1)})"
            f"({math.floor(farthest_x1)}, {math.floor(farthest_y1)})")
    else:
        closest_x2, closest_y2, farthest_x2, farthest_y2 = closest_point(def_x3, def_y3, def_x4, def_y4)
        print(
            f"({math.floor(closest_x2)}, {math.floor(closest_y2)})"
            f"({math.floor(farthest_x2)}, {math.floor(farthest_y2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
