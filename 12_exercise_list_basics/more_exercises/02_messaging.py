# input
numbers_sequence = input().split()
text = list(input())

# variable
message = ""

# logic
for number in numbers_sequence:
    index_sum = 0
    for char in number:
        index_sum += int(char)
    index = index_sum % len(text)
    message += text[index]
    text.pop(index)

# output
print(message)
