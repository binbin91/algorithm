# -*- coding: utf-8 -*-

from collections import deque


# 借助队列(先进先出)进行层序遍历, 当左右孩子都为空时, 说明到最底一层了
# PS: 最小深度是从根节点到最近叶子节点的最短路径的节点数量, 注意是叶子节点, 左右孩子都为空的节点才是叶子节点!!!
def aa(root):
    if not root: return 0
    res, queue = 1, deque([root])
    while queue: 
        res += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if not node.left and not node.right: return res
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return res


def bb(root):
    if not root: return 0
    queue = deque([root, 1])
    while queue:
	node, res = queue.popleft()
        if not node.left and not node.right:
	    return res
	if node.left:
	    queue.append((node.left, res + 1))
	if node.right:
            queue.append((node.right, res + 1))
    return 0
