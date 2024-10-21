# input
n = int(input())
word = input()
strings = []

# logic
for i in range(n):
    current_string = input()
    strings.append(current_string)

filter_string = []

for current_string in strings:
    if word in current_string:
        filter_string.append(current_string)

# output
print(strings)
print(filter_string)
