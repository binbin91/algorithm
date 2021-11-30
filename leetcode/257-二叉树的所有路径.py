# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    stack, path, res = deque([root]), deque([str(root.val)]), []
    while stack:
        node = stack.pop()
        p = path.pop()
        if not (node.left or node.right): 
            res.append(p)
        if node.right:
            stack.append(node.right)
            path.append(p + '->' + str(node.right.val))
        if node.left:
            stack.append(node.left)
            path.append(p + '->' + str(node.left.val))
    return res
