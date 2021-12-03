# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

def aa(root, val):
    if not root: return TreeNode(val)
    if val < root.val: root.left = aa(root.left, val)
    if root.val > val: root.right = aa(root.right, val)
    return root

def bb(root, val):
    if not root: return TreeNode(val)
    pre, cur = None, root
    while cur:
        if cur.val < val: pre, cur = cur, cur.right
        elif cur.val > val: pre, cur = cur, cur.left
    if pre.val > val: pre.left = TreeNode(val)
    else: pre.right = TreeNode(val) 
    return root
