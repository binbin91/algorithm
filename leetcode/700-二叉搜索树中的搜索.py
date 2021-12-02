# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

def aa(root, val):
    if not root or root.val == val: return root
    if root.val > val: aa(root.left, val)
    if root.val < val: aa(root.right, val)

def bb(root, val):
    while root:
        if val < root.val: root = root.left
        elif val > root.val: root = root.right
        else: return root
    return root
