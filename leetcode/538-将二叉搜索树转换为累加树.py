# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

def aa(root):
    def recur(root):
        if not root: return
        recur(root.right)
        root.val += pre.val
        pre = root
        recur(root.left)
    pre = TreeNode()
    recur(root)
    return root
