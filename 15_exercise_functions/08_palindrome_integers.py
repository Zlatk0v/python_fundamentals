def is_palindrome(def_number):
    return str(def_number) == str(def_number)[::-1]


def check_palindromes(def_numbers):
    numbers_list = def_numbers.split(", ")
    results = [is_palindrome(num) for num in numbers_list]
    for result in results:
        print(result)


numbers = input()
check_palindromes(numbers)
