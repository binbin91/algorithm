# -*- coding: utf-8 -*-

# DFS
# 深度 = max(左子树深度, 右子树深度) + 1
def aa(root):
    if not root: return 0
    return max(aa(root.left), aa(root.right)) + 1

# BFS
def bb(root):
    if not root: return 0
    queue, res = [root], 0
    while queue:
        tmp = []
        for i in queue:
            if i.left: tmp.append(i.left) 
            if i.right: tmp.append(i.right) 
        queue = tmp
        res += 1
    return res
