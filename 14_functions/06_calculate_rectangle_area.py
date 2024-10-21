def rectangle_area(max_width, max_height):
    area = max_width * max_height
    return area


width = int(input())
height = int(input())
print(f"{rectangle_area(width, height)}")
