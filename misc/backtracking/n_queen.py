# The n queen is the problem of placing n queens on a NxN chessboard so that
# no queens can attack each other.


def is_conf_valid(board, x, y, n):
    column_sum = 0
    for i in range(n):
        column_sum += board[i][y]

    return sum(board[x]) <= 1 and column_sum <= 1


def place_queens(chessboard, conf, queens, n):
    if queens == n:
        return True

    x, y = conf
    if x < n and y < n:
        chessboard[x][y] += 1
    else:
        return False

    if is_conf_valid(chessboard, *conf, n):
        return place_queens(chessboard, conf, queens+1, n)
    else:
        chessboard[x][y] -= 1

        left = place_queens(chessboard, (x, y + 1), queens, n)
        if not left:
            return place_queens(chessboard, (x + 1, y), queens, n)
        return left


def n_queens(n):
    chessboard = [[0 for _ in range(n)] for _ in range(n)]

    place_queens(chessboard, (0, 0), 0, len(chessboard))
    return chessboard


print(n_queens(10))
