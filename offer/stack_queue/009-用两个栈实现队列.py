# -*- coding: utf-8 -*-

# 栈底无法直接删除元素, 需要将上方元素全部出栈
# 双栈实现列表倒序
# 利用栈B删除队首, B出栈=A删除栈底

class CQueue(object):
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, v):
        self.A.append(v)

    def deleteHead(self):
        # 若栈B不为空, 直接返回栈顶
        if self.B: return self.B.pop()
        # 若栈A为空，直接返回-1
        if not self.A: return -1
        # A元素全部转移到B, 实现倒序, 返回B栈顶
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
