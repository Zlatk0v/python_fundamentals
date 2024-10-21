input_string = input()
numbers = []
non_numbers = []

for char in input_string:
    if char.isdigit():
        numbers.append(int(char))
    else:
        non_numbers.append(char)
take_list = [numbers[i] for i in range(0, len(numbers), 2)]
skip_list = [numbers[i] for i in range(1, len(numbers), 2)]
result = []
current_index = 0
for take, skip in zip(take_list, skip_list):
    result.extend(non_numbers[current_index:current_index + take])
    current_index += take + skip
print("".join(result))
