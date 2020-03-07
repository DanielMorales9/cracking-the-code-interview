class Node:
    next = None
    value = None

    def __init__(self, value):
        self.value = value

    @staticmethod
    def initialize(values):
        node = Node(values[0])
        for i in values[1:]:
            node.list_append(i)
        return node

    def list_append(self, d):
        end = Node(d)
        n = self
        while n.next:
            n = n.next
        n.next = end

    def __repr__(self):
        s = "["
        n = self
        while n.next:
            s += "%s, " % n.value
            n = n.next
        s += "%s" % n.value
        s += "]"
        return s

    # 2.1a
    def remove_duplicates(self):
        d = {self.value}
        n = self.next
        prev = self
        while n.next:
            if n.value in d:
                prev.next = n.next
                n = prev.next
            else:
                d.add(n.value)
                prev = prev.next
                n = n.next

        if n.value in d:
            prev.next = None

    @staticmethod
    def delete_all(head, d):
        n = head
        if n.value == d:
            head = head.next

        while n.next:
            if n.next.value == d:
                n.next = n.next.next
            n = n.next

        return head

    def length(self):
        cnt = 1
        n = self
        while n.next:
            cnt += 1
            n = n.next
        return cnt

    # 2.1b
    def remove_duplicates_1(self):
        n = self
        while n:
            head = self.delete_all(n.next, n.value)
            n.next = head
            n = n.next

    # 2.2
    def nth(self, nth):
        n = self
        i = 0
        while n.next:
            if i == nth:
                return n
            i += 1
            n = n.next
        return None

    # 2.3
    @staticmethod
    def delete_from_me(n):
        if not n:
            return

        while n.next.next:
            n.value = n.next.value
            n = n.next

        n.value = n.next.value
        n.next = None

    # 2.4
    def sum_digits(self, digits):

        def rec(s1, s2):
            if s1.next and s2.next:
                node = rec(s1.next, s2.next)
            else:
                return Node(s1.value + s2.value)

            d = node.value // 10
            node.value %= 10
            acc = d
            acc += s2.value + s1.value
            n = Node(acc)
            n.next = node
            return n

        right_len = self.length()
        left_len = digits.length()
        if right_len > left_len:
            to_align = self
            fine = digits
        elif right_len < left_len:
            to_align = digits
            fine = self
        else:
           return rec(self, digits)

        diff = abs(right_len - left_len)
        head = Node(to_align.value)
        curr = head
        to_align = to_align.next
        while diff > 1:
            curr.next = Node(to_align.value)
            curr = curr.next
            to_align = to_align.next
            diff -= 1

        node = rec(to_align, fine)
        curr.next = node
        return head

    # 2.5
    def find_circular(self):
        a = self
        b = self

        while b.next:
            a = a.next
            b = b.next.next
            if a == b:
                break

        if not b.next:
            return None

        a = self
        while a != b:
            a = a.next
            b = b.next

        return b


node = Node.initialize([1] * 2 + [2] * 2)
node.remove_duplicates()
print(node)
node.remove_duplicates()

node = Node.initialize([1] * 2 + [2] * 2)
node.remove_duplicates_1()
print(node)

node = Node.initialize(range(4))
print(node.nth(2))

node = Node.initialize(range(4))
node.delete_from_me(node.nth(2))
print(node)

s1 = Node.initialize([3, 1, 5])
s2 = Node.initialize([2, 1])
print(s2, s1)
print(s2.sum_digits(s1))


c = Node.initialize(range(1, 7))
third = c.next.next
last = c
while last.next:
    last = last.next

last.next = third

print(c.find_circular().value)
