# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    if not root: return []
    queue = deque([root])
    while queue: 
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            if node.left: queue.extend(node.left)
            if node.right: queue.extend(node.right)
            if i == n-1: break
            node.next = queue[0]
    return root
