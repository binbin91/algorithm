# -*- coding: utf-8 -*-

from collections import deque


# 借助队列(先进先出)进行层序遍历, 在层序遍历时, 计算每层总和, 再将每层均值放入res数组
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
