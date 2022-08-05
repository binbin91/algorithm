# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 已知二叉搜索树:
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

# 遇到空节点返回即可
# 若root.val < low, 递归右子树, 并返回右子树符合条件的头节点
# 若root.val > high, 递归左子树, 并返回左子树符合条件的头节点

def aa(root, low, high):
    if not root: return
    if root.val < low: return aa(root.right, low, high) 
    if high > root.val: return aa(root.left, low, high)
    if low <= root.val <= high:
        root.left = aa(root.left, low, high)
        root.right = aa(root.right, low, high)
        return root
