# -*- coding: utf-8 -*-

from collections import deque


class MyStack(object):
    def __init__(self):
        self.q_in, self.q_out = deque(), deque()

    def push(self, x):
        self.q_in.append(x)

    def pop(self):
        if self.empty(): return

        for i in range(len(self.q_in)-1):
            self.q_out.append(self.q_in.popleft())

        self.q_in, self.q_out = self.q_out, self.q_in
        return self.q_out.popleft()

    def top(self):
        if self.empty(): return
        return self.q_in[-1]

    def empty(self):
        return len(self.q_in) == 0

if __name__ == "__main__":
    q = MyStack()
    q.push(1)
    q.push(2)
    print q.pop()
    q.push(3)
    q.push(4)
    print q.pop()
    print q.pop()
    print q.pop()
    print q.empty()
