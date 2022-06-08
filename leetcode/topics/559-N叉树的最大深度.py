# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    if not root: return 0
    res, queue = 0, deque([root])
    while queue: 
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.children: queue.extend(node.children)
        res += 1
    return res
