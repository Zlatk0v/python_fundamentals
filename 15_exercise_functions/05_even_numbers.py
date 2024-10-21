def is_even(max_number):
    return max_number % 2 == 0


numbers_as_string = input().split()
numbers_as_integers = []
for number in numbers_as_string:
    numbers_as_integers.append(int(number))
final_list = []
for current_number in numbers_as_integers:
    if is_even(current_number):
        final_list.append(current_number)
print(final_list)
