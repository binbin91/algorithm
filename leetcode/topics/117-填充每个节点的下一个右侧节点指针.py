# -*- coding: utf-8 -*-

from collections import deque


# 借助队列(先进先出)进行层序遍历, 每层遍历时让尾节点指向当前节点, 让当前节点成为尾节点
def aa(root):
    if not root: return []
    queue = deque([root])
    while queue: 
        tail = None
        for _ in range(len(queue)):
            node = queue.pop(0)
            if tail: tai.next = node
            tail = node
            if node.left: queue.extend(node.left)
            if node.right: queue.extend(node.right)
    return root
