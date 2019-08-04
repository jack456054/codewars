def isSolved(board):
    finish_or_not = True

    # Check row:
    for line in board:
        winner, finish_or_not = check_line(line, finish_or_not)
        if winner == 1 or winner == 2:
            return winner

    # Check column:
    for col in range(0, 3):
        winner, finish_or_not = check_line([board[0][col], board[1][col], board[2][col]], finish_or_not)
        if winner == 1 or winner == 2:
            return winner

    # Check diagonal:
    winner, finish_or_not = check_line([board[0][0], board[1][1], board[2][2]], finish_or_not)
    if winner == 1 or winner == 2:
        return winner
    winner, finish_or_not = check_line([board[0][2], board[1][1], board[2][0]], finish_or_not)
    if winner == 1 or winner == 2:
        return winner

    return 0 if finish_or_not else -1


def check_line(line, finish_or_not):
    if (len(set(line)) == 1 and (set(line) == {1} or set(line) == {2})):
        return line[0], True
    for block in line:
        if block == 0:
            finish_or_not = False
    return -1, finish_or_not


if __name__ == '__main__':
    # not yet finished(-1)
    board = [[0, 0, 1],
             [0, 1, 2],
             [2, 1, 0]]
    print(isSolved(board))

    # winning row(1 or 2)
    board = [[1, 1, 1],
             [0, 2, 2],
             [0, 0, 0]]
    print(isSolved(board))

    # winning column(1 or 2)
    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 1, 2]]
    print(isSolved(board))

    # draw(0)
    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 2, 1]]
    print(isSolved(board))
