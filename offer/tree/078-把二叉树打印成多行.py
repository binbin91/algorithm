# -*- coding: utf-8 -*-

import collections

# JZ22变形题, 利用for循环与临时队列存储当前层的结果
def aa(root):
    if not root: return []
    res, queue = [], collections.deque([root])
    while queue:
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(tmp.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(tmp)
    return res
