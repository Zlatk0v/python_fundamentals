# input
divisor = int(input())
boundary = int(input())

# variables
number = ''

# logic
for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        break

# output
print(number)
