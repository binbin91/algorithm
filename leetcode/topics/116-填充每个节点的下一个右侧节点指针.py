# -*- coding: utf-8 -*-

from collections import deque


# 借助队列(先进先出)进行层序遍历, 每层遍历时记录下本层根节点, 然后在遍历时让前一个节点指向本节点即可
def aa(root):
    if not root: return []
    queue = deque([root])
    while queue: 
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            if node.left: queue.extend(node.left)
            if node.right: queue.extend(node.right)
            if i == n-1: break
            node.next = queue[0]
    return root
