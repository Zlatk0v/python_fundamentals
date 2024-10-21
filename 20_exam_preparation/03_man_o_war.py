def fire(ship_sections, current_command:list):
    index, damage = int(current_command[1]), int(current_command[2])
    if index in range(len(ship_sections)):
        ship_sections[index] -= damage
        if ship_sections[index] <= 0:
            return ship_sections, True
    return ship_sections, False


def defend(ship_sections: list, current_command: list) -> list and bool:
    start_index, end_index, damage = int(current_command[1]), int(current_command[2]), int(current_command[3])
    if start_index in range(len(ship_sections)) and end_index in range(len(ship_sections)):
        for section_index in range(start_index, end_index + 1):
            ship_sections[section_index] -= damage
            if ship_sections[section_index] <= 0:
                return ship_sections, True
    return ship_sections, False


def repair(ship_sections: list, current_command: list, max_health:int) -> list and bool:
    index, health = int(current_command[1]), int(current_command[2])
    if index in range(len(ship_sections)):
        ship_sections[index] += health
        if ship_sections[index] > max_health:
            ship_sections[index] = max_health
    return ship_sections


def status(ship_sections: list, max_health: int) -> str:
    count = 0
    for index in range(len(prate_ship_sections)):
        if prate_ship_sections[index] < max_health / 5:
            count += 1
    return f"{count} sections need repair."


# input
prate_ship_sections = [int(section) for section in input().split(">")]
war_ship_sections = [int(section) for section in input().split(">")]
max_health_per_section = int(input())

# variables
prate_ship_has_sunken = False
war_ship_has_sunken = False

# logic and output
command = input().split()
while "Retire" not in command:
    action = command[0]
    if action == "Fire":
        war_ship_sections, war_ship_has_sunken = fire(war_ship_sections, command)
        if war_ship_has_sunken:
            break
    elif action == "Defend":
        prate_ship_sections, prate_ship_has_sunken = defend(prate_ship_sections, command)
        if prate_ship_has_sunken:
            break
    elif action == "Repair":
        prate_ship_sections = repair(prate_ship_sections, command, max_health_per_section)
    elif action == "Status":
        print(status(prate_ship_sections, max_health_per_section))
    command = input().split()
if war_ship_has_sunken:
    print("You won! The enemy ship has sunken.")
elif prate_ship_has_sunken:
    print("You lost! The pirate ship has sunken.")
else:
    print(f"Pirate ship status: {sum(prate_ship_sections)}")
    print(f"Warship status: {sum(war_ship_sections)}")
