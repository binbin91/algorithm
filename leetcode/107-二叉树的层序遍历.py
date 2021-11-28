# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    if not root: return []
    res, queue = [], deque([root])
    while queue: 
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(tmp)
    res.reverse()
    return res
