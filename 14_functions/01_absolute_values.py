def absolute_values(func_sequence):

    numbers = sequence.split()
    abs_numbers = [abs(float(num)) for num in numbers]
    print(abs_numbers)


sequence = input()
absolute_values(sequence)
