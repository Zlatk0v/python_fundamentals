def check_winner(board):
    size = len(board)
    for row in board:
        if row.count(row[0]) == size and row[0] != 0:
            return row[0]
    for col in range(size):
        col_values = [board[row][col] for row in range(size)]
        if col_values.count(col_values[0]) == size and col_values[0] != 0:
            return col_values[0]
    if all(board[i][i] == board[0][0] for i in range(size)) and board[0][0] != 0:
        return board[0][0]
    if all(board[i][size - i - 1] == board[0][size - 1] for i in range(size)) and board[0][size - 1] != 0:
        return board[0][size - 1]
    return 0


current_board = []
for _ in range(3):
    input_row = list(map(int, input().split()))
    current_board.append(input_row)

winner = check_winner(current_board)

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
