# -*- coding: utf-8 -*-

import collections

def aa(root):
    if not root: return []
    res, queue = [], collections.deque([root])
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return res
