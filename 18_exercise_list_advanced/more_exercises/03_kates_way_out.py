n_rows = int(input())
maze = [list(input()) for _ in range(n_rows)]

kate_row, kate_col = -1, -1
for row in range(n_rows):
    for col in range(len(maze[row])):
        if maze[row][col] == 'k':
            kate_row, kate_col = row, col
            break
    if kate_row != -1:
        break

stack = [(kate_row, kate_col, 1)]
max_escape_moves = 0

while stack:
    current_row, current_col, current_move_count = stack.pop()

    if (current_row == 0 or current_row == n_rows - 1 or
            current_col == 0 or current_col == len(maze[0]) - 1):
        max_escape_moves = max(max_escape_moves, current_move_count)

    original_cell = maze[current_row][current_col]
    maze[current_row][current_col] = '#'

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        next_row = current_row + dr
        next_col = current_col + dc

        if (0 <= next_row < n_rows and 0 <= next_col < len(maze[0]) and
                maze[next_row][next_col] == ' '):
            stack.append((next_row, next_col, current_move_count + 1))

    maze[current_row][current_col] = original_cell

if max_escape_moves == 0:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {max_escape_moves} moves")
