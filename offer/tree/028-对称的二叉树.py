# -*- coding: utf-8 -*-

# 对称二叉树:
#   1. 对称节点值相等
#   2. 左子节点和右子节点对称
#   3. 右子节点和左子节点对象
def aa(root):
    def recur(l, r):
        if not l and not r: return True
        if not l or not r or l.val != r.val: return False
        return recur(l.left, r.right) and recur(l.right, r.left)
    return recur(root.left, root.right) if root else True
