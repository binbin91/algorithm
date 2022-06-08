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
            if node.left: queue.extend(node.left)
            if node.right: queue.extend(node.right)
        res.append(max(tmp))
    return res
