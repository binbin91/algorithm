# -*- coding: utf-8 -*-


def aa(root):
    if not root: return []
    stack = [root] 
    while stack: 
        node = stack.pop()
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
        node.left, node.right = node.right, node.left
    return root 
