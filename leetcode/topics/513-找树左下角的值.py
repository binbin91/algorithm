# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    if not root: return
    res, queue = 0, deque([root])    
    while queue:
        qs = len(queue)
        for i in range(qs):
            if i == 0: res = queue[i].val
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return res
