from typing import List


class Node:
    data = None
    next = None

    def __init__(self, value):
        self.data = value


class Stack:
    top: Node = None
    size = 0

    def pop(self):
        if self.top:
            item = self.top.data
            self.top = self.top.next
            self.size -= 1
            return item
        return None

    def push(self, item):
        t = Node(item)
        t.next = self.top
        self.top = t
        self.size += 1

    def peek(self):
        if self.top:
            return self.top.data
        return None

    def sort(self):
        r = Stack()
        while self.size > 0:
            item = self.pop()
            while r.size > 0 and r.peek() > item:
                self.push(r.pop())
            r.push(item)

        self.top = r.top

    def __repr__(self):
        top = self.top
        s = []
        while top:
            if top.data:
                s.append(str(top.data))
            top = top.next

        return ", ".join(s)


s = Stack()
[s.push(a) for a in range(5)]
[s.push(a) for a in range(10, 5, -1)]
print(s)
s.sort()
print(s)


class Queue:
    first: Node = None
    last: Node = None

    def enqueue(self, item):
        if self.first:
            last = Node(item)
            self.first = last
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    def dequeue(self):
        if self.first:
            item = self.first.data
            self.first = self.first.next
            return item
        return None


# 3.1 Describe how you could use a single array to implement three t_stacks
class ThreeStack:
    size = 3
    array: List = [None] * size
    top = [None, None, None]

    def pop(self, stack_num):
        if self.top[stack_num]:
            if self.top[stack_num] is None:
                self.top[stack_num] = stack_num

            item = self.array[self.top[stack_num]]
            self.array[self.top[stack_num]] = None
            if self.top[stack_num] != stack_num:
                self.top[stack_num] += 3
            return item
        return None

    def push(self, stack_num, item):
        offset = 3
        if self.top[stack_num] is None:
            self.top[stack_num] = stack_num
            offset = 0

        elif self.top[stack_num] + offset >= len(self.array):
            self.array += [None] * self.size

        self.top[stack_num] += offset
        self.array[self.top[stack_num]] = item

    def __repr__(self):
        a = "Stack #0 [ " + ' | '.join([str(a) for a in self.array[0::3] if
                                       a]) + " ]"
        b = "Stack #1 [ " + ' | '.join([str(a) for a in self.array[1::3] if
                                       a]) + " ]"
        c = "Stack #2 [ " + ' | '.join([str(a) for a in self.array[2::3] if
                                       a]) + " ]"
        return a + "\n" + b + "\n" + c


t_stacks = ThreeStack()

t_stacks.push(0, 1)
t_stacks.push(1, 2)
t_stacks.push(2, 3)

t_stacks.push(1, 4)
t_stacks.push(1, 10)
t_stacks.pop(1)

print(t_stacks)


# 3.2
class MinStack:
    top: Node = None
    min: Node = None

    def pop(self):
        if self.top:
            item = self.top.data
            self.top = self.top.next
            self.min = self.min.next
            return item

        return None

    def push(self, item):
        t = Node(item)
        if self.top is not None:
            m = Node(min(item, self.min.data))
        else:
            m = Node(item)

        t.next = self.top
        m.next = self.min
        self.top = t
        self.min = m

    def __repr__(self):
        t = self.top
        m = self.min
        s = []
        while t:
            s.append(f"{t.data}, {m.data}")
            t = t.next
            m = m.next
        return "\n".join(s)


stack = MinStack()

print("push")
[stack.push(a) for a in range(-10, 1)]
print(stack)
print("pop")
print([stack.pop() for _ in range(5)])
print(stack)

class SetOfStacks:
    stacks: List[Stack] = []
    max_size = 10

    def push(self, item):
        if self.stacks:
            current_stack = self.stacks[-1]
            if current_stack.size == self.max_size:
                current_stack = Stack()
                self.stacks.append(current_stack)
        else:
            current_stack = Stack()
            self.stacks.append(current_stack)
        current_stack.push(item)

    def pop(self):
        if self.stacks:
            current_stack = self.stacks[-1]
            var = current_stack.pop()
            if current_stack.size == 0:
                self.stacks.pop()
            return var
        else:
            return None


class Tower:

    def __init__(self, n=0):
        self.stack = Stack()
        [self.stack.push(i) for i in range(n, 0, -1)]

    def move_to_disk(self, n, destination, buffer):
        if n > 0:
            self.move_to_disk(n - 1, buffer, destination)
            self.move_to_top(destination)
            buffer.move_to_disk(n - 1, destination, self)

    def move_to_top(self, destination):
        item = self.stack.pop()
        destination.add(item)

    def add(self, item):
        self.stack.push(item)

    def __repr__(self):
        return self.stack.__repr__()


one = Tower(5)
two = Tower()
three = Tower()

one.move_to_disk(5, three, two)

print("one")
print(one)

print("two")
print(two)

print("three")
print(three)


class QueueTwoStack:

    def __init__(self):
        self.enq = Stack()
        self.deq = Stack()

    def enqueue(self, item):
        buffer = Stack()
        el = self.deq.pop()
        while el:
            buffer.push(el)
            el = self.deq.pop()

        buffer.push(item)
        el = buffer.pop()
        while el:
            self.deq.push(el)
            el = buffer.pop()

        self.enq.push(item)

    def dequeue(self):
        buffer = Stack()
        el = self.enq.pop()
        while el:
            buffer.push(el)
            el = self.enq.pop()

        _ = buffer.pop()
        el = buffer.pop()
        while el:
            self.enq.push(el)
            el = buffer.pop()

        return self.deq.pop()

    def __repr__(self):
        return self.deq.__repr__()


q = QueueTwoStack()
print('Enqueue')
[q.enqueue(a) for a in range(1, 10)]
print(q)
print('Dequeue')
[q.dequeue() for _ in range(5)]
print(q)
