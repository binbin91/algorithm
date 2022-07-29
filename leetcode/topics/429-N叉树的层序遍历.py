# -*- coding: utf-8 -*-

from collections import deque


# 借助队列(先进先出)进行层序遍历, 和102大致相似
def aa(root):
    if not root: return []
    res, queue = [], deque([root])
    while queue: 
        tmp = [] 
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node.val)
            if node.children: queue.extend(node.children)
        res.append(tmp)
    return res
