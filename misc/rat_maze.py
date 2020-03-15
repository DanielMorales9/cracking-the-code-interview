# The Rat in a Maze
# A maze is given as N*N binary matrix of blocks where source is the upper
# left most block and the destination is the lower rightmost block. A Rat
# starts from the source and has to reach the destination. The rat can move
# only forward and down. The maze matrix has either dead blocks or free
# blocks. The goal is to return the path the rat will use to reach the end.


def find_path(maze, source, end):
    src_x, src_y = source

    if src_x >= len(maze) or src_y >= len(maze[0]):
        return None

    if maze[src_x][src_y] == 0:
        return None
    
    if source == end:
        return [source, end]

    # go down
    down = (src_x + 1, src_y)
    path = find_path(maze, down, end)
    if path:
        return [source] + path

    up = (src_x, src_y + 1)
    path = find_path(maze, up, end)
    if path:
        return [source] + path

    return None


maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

print(find_path(maze, (0, 0), (3, 3)))
