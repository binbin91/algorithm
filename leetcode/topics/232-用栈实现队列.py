# -*- coding: utf-8 -*-

class MyQueue(object):
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x):
        self.A.append(x)

    def pop(self):
        if self.empty(): return
        if self.B: return self.B.pop()
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()

    def peek(self):
        ans = self.pop()
        self.B.append(ans)
        return ans

    def empty(self):
        return not (self.A or self.B)

if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print q.peek()
    print q.pop()
    print q.empty()
