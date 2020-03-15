from copy import copy


def binary_search_tree(array):
    if array:
        center = len(array) // 2
        left = binary_search_tree(array[:center])
        right = binary_search_tree(array[center+1:])
        return Tree(value=array[center], left=left, right=right)

    return None


def inorder_successor(self, e):
    if e:
        if not e.parent and e.right:
            p = e.right.left_most_child()
        else:
            p = e.parent
            while e.parent:
                if p.left == e:
                    break
                e = p

        return p

    return None


def first_common_ancestor(a, b):
    while a:
        pa = a.parent
        bi = b
        while bi.parent:
            if bi.parent == pa:
                return bi.parent
            bi = bi.parent
        a = pa

    return None


def contains(root, a):
    if root:
        if root == a:
            return True
        return contains(root.left, a) or contains(root.left, a)
    return False


def first_common_ancestor_without_parent(root, a, b):
    if contains(root.left, a) and contains(root.left, b):
        return first_common_ancestor_without_parent(root.left, a, b)
    elif contains(root.right, a) and contains(root.right, a):
        return first_common_ancestor_without_parent(root.right, a, b)
    return root


def match_tree(r1, r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    if r1.value != r2.value:
        return False
    return match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right)


def sub_tree(r1, r2):
    if not r1:
        return False
    if r1.value == r2.value:
        if match_tree(r1, r2):
            return True
    return sub_tree(r1.left, r2) or sub_tree(r1.right, r2)


def contains_tree(r1, r2):
    if not r2:
        return True
    else:
        return sub_tree(r1, r2)


def find_sum(root, sum):
    store = []

    def rec(tree, sum, buffer):
        if tree:
            buffer = copy(buffer)
            tmp = sum
            buffer.append(tree.value)
            for bi in reversed(buffer):
                tmp -= bi
                if tmp == 0:
                    store.append(copy(buffer))

            rec(root.left, sum, buffer)
            rec(root.right, sum, buffer)
    rec(root, sum, [])
    return store


class Tree:

    def __init__(self, value, left=None, right=None, parent=None):
        self.left = left
        self.value = value
        self.right = right
        self.parent = parent

    def max_depth(self):
        if self:
            if self.left and self.right:
                return 1 + max(self.left.max_depth(), self.right.max_depth())
            elif self.left:
                return self.left.max_depth() + 1
            elif self.right:
                return self.right.max_depth() + 1
            else:
                return 1
        return 0

    def min_depth(self):
        if self:
            if self.left and self.right:
                return 1 + min(self.left.min_depth(), self.right.min_depth())
            elif self.left:
                return self.left.min_depth() + 1
            elif self.right:
                return self.right.min_depth() + 1
            else:
                return 1

        return 0

    def balanced(self):
        return abs(self.max_depth() - self.min_depth()) <= 1

    def nodes_at_depth(self):
        nodes = []

        def rec(root, depth):
            if root:
                if depth >= len(nodes):
                    nodes.append([])

                nodes[depth].append(root.value)
                rec(root.left, depth+1)
                rec(root.right, depth+1)

        rec(self, 0)

        return nodes

    def left_most_child(self):
        e = self
        if self:
            while e.left: e = e.left
            return e
        return None

root = Tree(0)
left = root.left = Tree(1)
right = root.right = Tree(2)

print(root.balanced())


class Node:

    def __init__(self, value=1, adjacents=None):
        self.value = value
        self.adjacents = adjacents


class Graph:

    def __init__(self, nodes):
        self.nodes = nodes

    def exists_path(self, start, end):
        stack = [start]
        d = {n: False for n in self.nodes}

        while stack:
            s = stack.pop()
            d[s] = True
            if s == end:
                return True
            s.extend([n for n in s.adjacents if not d[s]])

        return False

