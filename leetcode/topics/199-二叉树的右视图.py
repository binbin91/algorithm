# -*- coding: utf-8 -*-

from collections import deque


# 借助队列(先进先出)进行层序遍历, 在执行层序遍历前, 取队列最后一个node(中左右), 将值放入res数组
def aa(root):
    if not root: return []
    res, queue = [], deque([root])
    while queue: 
        node = queue[-1]
        res.append(node.val)
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return res
