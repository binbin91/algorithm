# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

# 二叉树搜索求累加树, 换个角度就是有序数组, 求从后往前的累加数组
# 从树中可以看出累加顺序是右中左, 那么我们需要反中序遍历, 然后顺序累加即可

# 定义一个全局变量pre, 用来保存当前节点的前一个节点数值
# 遇到空节点返回
# 右中左遍历二叉树

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
        return recur(root)
