# -*- coding: utf-8 -*-


# 辅助栈
class MinStack(object):
    def __init__(self):
        self.a, self.b = [], []

    def push(self, val):
        self.a.append(val)
        if not self.b or self.b[-1] >= val:
            self.b.append(val)

    def pop(self):
        if self.a[-1] == self.b[-1]:
            self.b.pop()
        self.a.pop()

    def top(self):
        return self.a[-1]

    def getMin(self):
        return self.b[-1]

if __name__ == "__main__":
    q = MinStack()
    q.push(-2)
    q.push(0)
    q.push(-3)
    print q.getMin()
    q.pop()
    print q.top()
    print q.getMin()
