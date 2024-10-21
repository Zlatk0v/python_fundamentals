# input
input_string = input()

# logic
number_list = list(map(int, input_string.split(", ")))
non_zeros = [num for num in number_list if num != 0]
zeros = [num for num in number_list if num == 0]
result = non_zeros + zeros

# output
print(result)
