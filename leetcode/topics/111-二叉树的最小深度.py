# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    if not root: return 0
    res, queue = 1, deque([root])
    while queue: 
        res += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if not node.left and not node.right: return res
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return res
