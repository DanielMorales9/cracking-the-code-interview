# Given a partially filled 9×9 2D array ‘grid[9][9]’,
# the goal is to assign digits (from 1 to 9)
# to the empty cells so that every row, column,
# and subgrid of size 3×3 contains exactly one
# instance of the digits from 1 to 9.


def is_safe(c, grid, start_x, start_y):
    # check row
    if c in grid[start_x]:
        return False

    # check col
    for row in grid:
        if row[start_y] == c:
            return False

    # check box
    start_x -= start_x % 3
    start_y -= start_y % 3
    for i in range(3):
        for j in range(3):
            if grid[i+start_x][j+start_y] == c:
                return False

    return True


def get_unfilled(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return -1, -1


def sudoku(grid):
    start_x, start_y = get_unfilled(grid)

    if start_x == -1 and start_y == -1:
        return True

    for c in range(1, 10):
        if is_safe(c, grid, start_x, start_y):
            grid[start_x][start_y] = c
            if sudoku(grid):
                return True
            grid[start_x][start_y] = 0

    return False


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print(sudoku(grid))
print(grid)
