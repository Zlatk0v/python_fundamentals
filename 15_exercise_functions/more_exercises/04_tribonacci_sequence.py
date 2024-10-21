def tribonacci_sequence(n):
    sequence = [1, 1, 2]
    for i in range(3, n):
        next_value = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_value)
    print(' '.join(map(str, sequence[:n])))


num = int(input())
tribonacci_sequence(num)
