# input
gifts = input().split()

# logic
while True:
    command = input()
    if command == "No Money":
        break
    command_parts = command.split()
    action = command_parts[0]
    if action == "OutOfStock":
        gift_name = command_parts[1]
        gifts = ["None" if gift == gift_name else gift for gift in gifts]
    elif action == "Required":
        gift_name = command_parts[1]
        index = int(command_parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_name
    elif action == "JustInCase":
        gift_name = command_parts[1]
        gifts[-1] = gift_name

# output
print(" ".join([gift for gift in gifts if gift != "None"]))
