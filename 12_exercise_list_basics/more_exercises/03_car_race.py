# input
times = list(map(int, input().split()))

# logic
middle_index = len(times) // 2
left_time = 0
for i in range(middle_index):
    left_time += times[i]
    if times[i] == 0:
        left_time *= 0.8
right_time = 0
for i in range(len(times) - 1, middle_index, -1):
    right_time += times[i]
    if times[i] == 0:
        right_time *= 0.8
winner = "left" if left_time < right_time else "right"
winner_time = min(left_time, right_time)

# output
print(f"The winner is {winner} with total time: {winner_time:.1f}")
