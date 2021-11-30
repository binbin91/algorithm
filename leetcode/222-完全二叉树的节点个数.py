# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    def recur(root):
        if not root: return 0
        left = recur(root.left)
        right = recur(root.right)
        res = left + right + 1 
        return res
    return recur(root)

# 精简版
def bb(root):
    if not root: return 0
    return 1 + bb(root.left) + bb(root.right)
