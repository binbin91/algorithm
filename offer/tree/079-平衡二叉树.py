# -*- coding: utf-8 -*-

# 平衡二叉树: 左右子树的深度相差不过1
# 剪枝
def aa(root):
    def recur(root):
        if not root: return 0
        left = recur(root.left)
        if left == -1: return -1
        right = recur(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) <= 1 else -1
    return recur(root) != -1
