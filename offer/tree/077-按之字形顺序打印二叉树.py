# -*- coding: utf-8 -*-

import collections

# JZ60变形题, 若是偶数层对临时队列做倒序操作
def aa(root):
    if not root: return
    res, queue = [], collections.deque([root])
    while queue:
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(tmp[::-1] if len(res) % 2 else tmp)
