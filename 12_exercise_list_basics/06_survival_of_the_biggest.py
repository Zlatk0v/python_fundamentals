# input
numbers = input()
n = int(input())

# logic
numbers_list = list(map(int, numbers.split()))
for _ in range(n):
    numbers_list.remove(min(numbers_list))

# output
print(", ".join(map(str, numbers_list)))
