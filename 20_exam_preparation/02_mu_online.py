# input
rooms = input().split("|")

# variable
initial_health = 100
initial_bitcoins = 0
best_room = 0
you_have_died = False

# logic and output
for room in rooms:
    best_room += 1
    room = room.split()
    command, number = room[0], int(room[1])
    if command == "potion":
        temp_health = initial_health
        initial_health += number
        if initial_health > 100:
            initial_health = 100
        amount = initial_health - temp_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            you_have_died = True
            break
if you_have_died:
    print(f"You died! Killed by {command}.")
    print(f"Best room: {best_room}")
else:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
