# Given an undirected graph and a number m,
# determine if the graph can be colored with at most m colors such that
# no two adjacent vertices of the graph are colored with the same color.
# Here coloring of a graph means the assignment of colors to all vertices.
#
# Input:
# 1) A 2D array graph[V][V] where V is the number of vertices in graph and
#   graph[V][V] is adjacency matrix representation of the graph. A value
#   graph[i][j] is 1 if there is a direct edge from i to j,
#   otherwise graph[i][j] is 0.
#
# 2) An integer m which is the maximum number of colors that can be used.

# Output:
# An array color[V] that should have numbers from 1 to m. color[i] should
# represent the color assigned to the ith vertex.
# The code should also return false if the graph cannot be colored with m
# colors.


def is_safe(graph, vertices, vertex):
    my_color = vertices[vertex]
    for i, v in enumerate(graph[vertex]):
        if v == 1 and vertices[i] == my_color:
            return False

    return True


def m_colouring(graph, vertices, m=1, vertex=0):
    n_vertices = len(graph)
    if vertex == n_vertices:
        return True

    for colour in range(1, m+1):
        vertices[vertex] = colour
        if is_safe(graph, vertices, vertex):
            flag = m_colouring(graph, vertices, m, vertex + 1)
            if flag:
                return True
        else:
            vertices[vertex] = 0

    return False


graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
vertices = [0, 0, 0, 0]
print(m_colouring(graph, vertices, m=3))
print(vertices)
