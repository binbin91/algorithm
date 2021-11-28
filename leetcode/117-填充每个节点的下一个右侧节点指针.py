# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    if not root: return []
    queue = deque([root])
    while queue: 
        n, tail = len(queue), None
        for _ in range(n):
            node = queue.pop(0)
            if tail: tai.next = node
            tail = node
            if node.left: queue.extend(node.left)
            if node.right: queue.extend(node.right)
    return root
