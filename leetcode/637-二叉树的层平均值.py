# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    if not root: return []
    res, queue = [], deque([root])
    while queue: 
        sum, qs = 0, len(queue)
        for _ in range(qs):
            node = queue.popleft()
            sum += node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(sum/qs)
    return res
