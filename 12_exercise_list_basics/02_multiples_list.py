# input
factor = int(input())
count = int(input())
numbers = []

# logic
for multiplier in range(1, count + 1):
    numbers.append(factor * multiplier)

# output
print(numbers)
