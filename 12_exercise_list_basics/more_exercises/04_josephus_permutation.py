# input
people_input = input()
k = int(input())
people = list(map(int, people_input.split()))

# variables
result = []
index = 0

# logic
while len(people) > 0:
    index = (index + k - 1) % len(people)
    result.append(people.pop(index))

# output
print(f"[{','.join(map(str, result))}]")
