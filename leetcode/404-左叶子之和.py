# -*- coding: utf-8 -*-


def aa(root):
    if not root: return
    res, stack = 0, [root]    
    while stack:
        node = stack.pop()
        if node.left and not node.left.left and node.left.right:
            res += node.left.val
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res
