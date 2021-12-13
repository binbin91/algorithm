# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

class Solution(object):
    def __init__(self):
        self.pre = TreeNode()

    def convertBST(self, root):
        def recur(root):
            if not root: return
            recur(root.right)
            root.val += self.pre.val
            self.pre = root
            recur(root.left)
        recur(root)
        return root
