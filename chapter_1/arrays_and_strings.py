from collections import Counter

dup = "ababababa"
unq = "abcd"
empty = ""

# 1.1
def unique_char(string):
    d = dict()
    for c in string:
        if c in d:
            return False
        d[c] = 1
    return True


def unique_char1(string):
    sorted_string = sorted(string)
    for i, c in zip(range(1, len(sorted_string)), sorted_string[1:]):
        if c == sorted_string[i - 1]:
            return False
    return True


print(unique_char(dup))
print(unique_char(unq))
print(unique_char1(dup))
print(unique_char1(unq))

# 1.2
def remove_duplicates(string):
    i = len(string) - 1
    while i > 0:
        s = string[i]
        if s in string[:i-1]:
            string = string[:i] + string[i+1:]
        i -= 1
    return string


print(remove_duplicates(dup))
print(remove_duplicates(unq))
print(remove_duplicates(empty))


calendario = "calendario"
locandiera = "locandiera"


# 1.3
def is_anagram(a, b):
    # O(nlogn)
    return sorted(a) == sorted(b)


def is_anagram_1(a, b):
    # O(n)
    an = Counter(a)
    bn = Counter(b)
    return an == bn


print(is_anagram(calendario, locandiera))
print(is_anagram_1(calendario, locandiera))


matrix = [list(range(1, 4)), list(range(4, 7)), list(range(7, 10))]
bigger_matrix = [list(range(1, 5)),
                 list(range(5, 9)),
                 list(range(9, 13)),
                 list(range(13, 17))]


# 1.6
def rotate(matrix):
    N = len(matrix)
    new = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            new[j][N-i-1] = matrix[i][j]
    return new


def rotate_1(matrix):
    N = len(matrix)

    for i in range(N-1):
        for j in range(i, N-1-i):
            first = matrix[i][j]
            new_i, new_j = j, N-i-1
            second = matrix[new_i][new_j]
            matrix[new_i][new_j] = first
            new_i, new_j = new_j, N - new_i - 1
            third = matrix[new_i][new_j]
            matrix[new_i][new_j] = second
            new_i, new_j = new_j, N - new_i - 1
            fourth = matrix[new_i][new_j]
            matrix[new_i][new_j] = third
            matrix[i][j] = fourth

    return matrix


print(rotate(matrix))
print(rotate(bigger_matrix))
print(rotate_1(matrix))
print(rotate_1(bigger_matrix))

zeros = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]


# 1.7
def zero_col_row(row_mat):
    d = []
    R = len(row_mat)
    C = len(row_mat[0])

    for i in range(R):
        for j in range(C):
            if not row_mat[i][j]:
                d.append((i, j))

    for i, j in d:
        row_mat[i][:] = [0] * C
        for row in row_mat:
            row[j] = 0

    return row_mat


print(zero_col_row(zeros))


waterbottle = "waterbottle"
erbottlewat = "erbottlewat"


# 1.8
def is_rotate(s1, s2):
    return s1 in (s2+s2)


print(is_rotate(waterbottle, erbottlewat))
