# -*- coding: utf-8 -*-

from collections import deque

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 传入根节点, 若为空节点就返回0, 递归时先求左子树节点数量, 再求右子树节点数量, 最后取总和加1(加1是因为算上当前中间节点)

def aa(root):
    def recur(root):
        if not root: return 0
        left = recur(root.left)
        right = recur(root.right)
        res = left + right + 1 
        return res
    return recur(root)

# 精简版
def bb(root):
    if not root: return 0
    return 1 + bb(root.left) + bb(root.right)
