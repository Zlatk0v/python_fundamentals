# input
n = int(input())
positive = []
negative = []

# logic
for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

# output
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}\n' # To get the count of the positives, we can use the len function.
      f'Sum of negatives: {sum(negative)}') # To get the sum of the negatives, we can use the sum function.
