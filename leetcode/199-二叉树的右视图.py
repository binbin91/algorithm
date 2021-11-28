# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    if not root: return []
    res, queue = [], deque([root])
    while queue: 
        node = queue[-1]
        res.append(node.val)
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return res
