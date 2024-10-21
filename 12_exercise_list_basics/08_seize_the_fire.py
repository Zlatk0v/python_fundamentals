# input
fire_cells = input().split("#")
water = int(input())

# variables
valid_cells = []
total_effort = 0
total_fire = 0

# logic
for fire in fire_cells:
    fire_type, value = fire.split(" = ")
    value = int(value)
    if fire_type == "High" and 81 <= value <= 125:
        is_valid = True
    elif fire_type == "Medium" and 51 <= value <= 80:
        is_valid = True
    elif fire_type == "Low" and 1 <= value <= 50:
        is_valid = True
    else:
        is_valid = False
    if is_valid and water >= value:
        water -= value
        valid_cells.append(value)
        effort = value * 0.25
        total_effort += effort
        total_fire += value

# output
print(f"Cells:\n - " + "\n - ".join(map(str, valid_cells)))
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
