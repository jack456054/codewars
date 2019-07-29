def done_or_not(board):
    # check rows:
    for index, _ in enumerate(board):
        check_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for index2, value in enumerate(board[index]):
            if value in check_board:
                check_board.remove(value)
            else:
                return 'Try again!'

    # check columns:
    for index, _ in enumerate(board):
        check_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for col_index in range(0, 9):
            if board[col_index][index] in check_board:
                check_board.remove(board[col_index][index])
            else:
                return 'Try again!'

    # check regions:
    for col_fixed_index in range(0, 3):
        for row_fixed_index in range(0, 3):
            check_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for row_index in range(0, 3):
                for col_index in range(0, 3):
                    if board[row_fixed_index * 3 + row_index][col_fixed_index * 3 + col_index] in check_board:
                        check_board.remove(board[row_fixed_index * 3 + row_index][col_fixed_index * 3 + col_index])
                    else:
                        return 'Try again!'

    return 'Finished!'


if __name__ == '__main__':
    print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8], [4, 9, 8, 2, 6, 1, 3, 7, 5], [7, 5, 6, 3, 8, 4, 2, 1, 9], [6, 4, 3, 1, 5, 8, 7, 9, 2], [5, 2, 1, 7, 9, 3, 8, 4, 6], [9, 8, 7, 4, 2, 6, 5, 3, 1], [2, 1, 4, 9, 3, 5, 6, 8, 7], [3, 6, 5, 8, 1, 7, 9, 2, 4], [8, 7, 9, 6, 4, 2, 1, 5, 3]]))
    print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8], [4, 9, 8, 2, 6, 1, 3, 7, 5], [7, 5, 6, 3, 8, 4, 2, 1, 9], [6, 4, 3, 1, 5, 8, 7, 9, 2], [5, 2, 1, 7, 9, 3, 8, 4, 6], [9, 8, 7, 4, 2, 6, 5, 3, 1], [2, 1, 4, 9, 3, 5, 6, 8, 7], [3, 6, 5, 8, 1, 7, 9, 2, 4], [8, 7, 9, 6, 4, 2, 1, 3, 5]]))
