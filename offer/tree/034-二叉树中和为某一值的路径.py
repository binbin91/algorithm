# -*- coding: utf-8 -*-

# 递归(前序遍历 + 路径记录)
def aa(root, sum):
    res, path = [], []
    def recur(root, tar):
        if not root: return 
        path.append(root.val)
        tar -= root.val
        if tar == 0 and not root.left and not root.right:
            res.append(list(path))
        recur(root.left, tar)
        recur(root.right, tar)
        path.pop()
    recur(root, sum)
    return res
