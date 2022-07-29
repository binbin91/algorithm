# -*- coding: utf-8 -*-

from collections import deque


# 借助队列(先进先出)进行层序遍历, 题目要求返回是自底向上的层次遍历, 最后就是将res数组反转下返回即可
def aa(root):
    if not root: return []
    res, queue = [], deque([root])
    while queue: 
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(tmp)
    res.reverse()
    return res
