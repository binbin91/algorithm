# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

def aa(root, l, h):
    if not root: return
    if root.val < l: return aa(root.right, l, h) 
    if h > root.val: return aa(root.left, l, h)
    if l <= root.val <= h:
        root.left = aa(root.left, l, h)
        root.right = aa(root.right, l, h)
        return root
