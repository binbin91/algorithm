# -*- coding: utf-8 -*-

from collections import deque


# 借助队列(先进先出)进行层序遍历, 层序遍历时记录下遍历的层数(层数=二叉树深度)
def aa(root):
    if not root: return 0
    res, queue = 0, deque([root])
    while queue: 
        tmp = []
        for i in range(queue):
            if i.left: tmp.append(i.left)
            if i.right: tmp.append(i.right)
        queue = tmp
        res += 1
    return res
