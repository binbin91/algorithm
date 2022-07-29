# -*- coding: utf-8 -*-


# 借助队列(先进先出)进行层序遍历, 层序遍历时获取一个节点, 开始交换此节点的左右节点
def aa(root):
    if not root: return []
    stack = [root] 
    while stack: 
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return root 
