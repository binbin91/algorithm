# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# JZ Offer 079
# 平衡二叉树定义: 左右子树的高度差绝对值不超过1
# 传入当前节点, 递归时节点为空返回0, 分别求出左右子树高度, 若差值小于等于1, 返回当前二叉树高度, 否则返回-1(表示不是二叉平衡树)

def aa(root):
    def recur(root):
        if not root: return 0
        left = recur(root.left)
        if left == -1: return -1
        right = recur(root.right)
        if right == -1: return -1
        return max(left, right)+1 if abs(left-right) <= 1 else -1
    return recur(root) >= 0
