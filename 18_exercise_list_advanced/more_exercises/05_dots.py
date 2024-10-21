n = int(input())

board = []
for _ in range(n):
    row = input().strip().split()
    board.append(row)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_connected_dots = 0

for row in range(n):
    for col in range(len(board[0])):
        if board[row][col] == '.':
            stack = [(row, col)]
            connected_count = 0

            while stack:
                current_row, current_col = stack.pop()
                if 0 <= current_row < n and 0 <= current_col < len(board[0]) and board[current_row][current_col] == '.':
                    connected_count += 1
                    board[current_row][current_col] = '-'
                    for direction_row, direction_col in directions:
                        stack.append((current_row + direction_row, current_col + direction_col))

            max_connected_dots = max(max_connected_dots, connected_count)

print(max_connected_dots)
