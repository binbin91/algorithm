# -*- coding: utf-8 -*-

from collections import deque


# 借助队列(先进先出)进行层序遍历, 将每一层中最大的值放入res数组即可
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
