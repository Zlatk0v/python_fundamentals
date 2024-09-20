# input
n = int(input())

# logic
for number in range(1, n + 1):
    sum_of_digits = 0
    current_number = number
    while current_number > 0:
        sum_of_digits += current_number % 10
        current_number //= 10
    is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11

# output
    print(f"{number} -> {is_special}")
