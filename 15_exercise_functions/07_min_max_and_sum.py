def process_numbers(top_sequence):
    numbers = list(map(int, top_sequence.split()))
    min_number = min(numbers)
    max_number = max(numbers)
    sum_of_numbers = sum(numbers)
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_of_numbers}")


sequence = input()
process_numbers(sequence)
