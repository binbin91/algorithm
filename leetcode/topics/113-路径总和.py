# -*- coding: utf-8 -*-


# JZ Tree 034
def aa(root, sum):
    res, path = [], []
    def recur(root, sum):
        if not root: return
        path.append(root.val)
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            res.append(list(path))
        recur(root.left, sum)
        recur(root.right, sum)
        path.pop()
    recur(root, sum)
    return res
