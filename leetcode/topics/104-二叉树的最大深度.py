# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    if not root: return 0
    res, queue = 0, deque([root])
    while queue: 
        tmp = []
        for i in range(queue):
            if i.left: tmp.append(i.left)
            if i.right: tmp.append(i.right)
        queue = tmp
        res += 1
    return res
