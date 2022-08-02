# -*- coding: utf-8 -*-


# 迭代法(前序遍历), 借助辅助栈来记录该节点, 以及头节点到该节点路径数值总和
def aa(root, sum):
    if not root: return False
    stack = [(root, root.val)]
    while stack:
        node, val = stack.pop() 
        if not node.left and not node.right and val == sum: 
            return True
        if node.right: 
            stack.append((node.right, val + node.right.val))
        if node.left: 
            stack.append((node.left, val + node.left.val))
    return False
