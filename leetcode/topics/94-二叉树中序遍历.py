# -*- coding: utf-8 -*-


# 递归
def aa(root):
    res = []
    def recur(root):
        if not root: return
        recur(root.left)
        res.append(root.val)
        recur(root.right)
    recur(root)
    return res


# 迭代
def bb(root):
    if not root: return []
    stack, res, cur = [], [], root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            stack.append(cur.val)
            cur = cur.right
    return res
