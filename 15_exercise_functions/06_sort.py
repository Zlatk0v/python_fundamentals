def sort_numbers(top_sequence):
    numbers = list(map(int, top_sequence.split()))
    sorted_numbers = sorted(numbers)
    return sorted_numbers


sequence = input()
print(sort_numbers(sequence))
