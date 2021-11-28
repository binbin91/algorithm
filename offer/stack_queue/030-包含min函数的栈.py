# -*- coding: utf-8 -*-

# 借助辅助栈B来存储栈A降序元素, 这样min只需返回栈B的栈顶即可
class MinStack(object):
    def __init__(self):
        self.A, self.B = [], []

    def push(self, v):
        self.A.append(v)
        if not self.B or self.B[-1] >= v:
            self.B.append(v)

    def pop(self):
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self):
        return self.A[-1]
    
    def min(self):
        return self.B[-1]
