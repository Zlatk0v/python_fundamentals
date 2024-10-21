lst = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "end":
        break

    if command[0] == "exchange":
        index = int(command[1])
        if 0 <= index < len(lst):
            lst = lst[index + 1:] + lst[:index + 1]
        else:
            print("Invalid index")

    elif command[0] == "max":
        even_odd = command[1]
        if even_odd == "even":
            filtered = [i for i in lst if i % 2 == 0]
        else:
            filtered = [i for i in lst if i % 2 != 0]

        if filtered:
            max_value = max(filtered)
            print(len(lst) - 1 - lst[::-1].index(max_value))
        else:
            print("No matches")

    elif command[0] == "min":
        even_odd = command[1]
        if even_odd == "even":
            filtered = [i for i in lst if i % 2 == 0]
        else:
            filtered = [i for i in lst if i % 2 != 0]

        if filtered:
            min_value = min(filtered)
            print(len(lst) - 1 - lst[::-1].index(min_value))
        else:
            print("No matches")

    elif command[0] == "first":
        count = int(command[1])
        even_odd = command[2]
        if even_odd == "even":
            filtered = [i for i in lst if i % 2 == 0]
        else:
            filtered = [i for i in lst if i % 2 != 0]

        if count > len(lst):
            print("Invalid count")
        else:
            print(filtered[:count])

    elif command[0] == "last":
        count = int(command[1])
        even_odd = command[2]
        if even_odd == "even":
            filtered = [i for i in lst if i % 2 == 0]
        else:
            filtered = [i for i in lst if i % 2 != 0]

        if count > len(lst):
            print("Invalid count")
        else:
            print(filtered[-count:])

print(lst)
