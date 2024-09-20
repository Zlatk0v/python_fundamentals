# input
event = input()

# variables
coffee_count = 0

# logic and output
while event != "END":
    if event == "coding" \
            or event == "dog" \
            or event == "cat" \
            or event == "movie":
        coffee_count += 1
    elif event == "CODING" \
            or event == "DOG" \
            or event == "CAT" \
            or event == "MOVIE":
        coffee_count += 2
    if coffee_count > 5:
        print("You need extra sleep")
        break
    event = input()
if coffee_count <= 5:
    print(coffee_count)
