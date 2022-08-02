# -*- coding: utf-8 -*-


# 迭代法(前序遍历)
# 左叶子判断: 若当前节点的左节点不为空, 但当前节点的左节点的左节点为空, 当前节点的左节点的右节点为空, 
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
