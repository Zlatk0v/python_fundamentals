def round_numbers(def_sequence):
    numbers = def_sequence.split()
    rounded_numbers = [round(float(num)) for num in numbers]
    return rounded_numbers


sequence = input()
print(round_numbers(sequence))
