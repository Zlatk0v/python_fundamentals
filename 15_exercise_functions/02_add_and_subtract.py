def sum_numbers(a, b):
    return a + b


def tract(sum_result, c):
    return sum_result - c


def add_tract(a, b, c):
    sum_result = sum_numbers(a, b)
    result = tract(sum_result, c)
    print(result)


first_num = int(input())
second_num = int(input())
third_num = int(input())
add_tract(first_num, second_num, third_num)
