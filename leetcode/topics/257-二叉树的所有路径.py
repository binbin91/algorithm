# -*- coding: utf-8 -*-

from collections import deque


# 迭代法(前序遍历)
# 借助辅助栈来存储遍历路径
def aa(root):
    stack, path, res = deque([root]), deque([str(root.val)]), []
    while stack:
        node, p = stack.pop(), path.pop()
        if not (node.left or node.right): 
            res.append(p)
        if node.right:
            stack.append(node.right)
            path.append(p + '->' + str(node.right.val))
        if node.left:
            stack.append(node.left)
            path.append(p + '->' + str(node.left.val))
    return res
