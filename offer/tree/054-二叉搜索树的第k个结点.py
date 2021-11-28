# -*- coding: utf-8 -*-

# 中序遍历倒序(先递归右子树)
def aa(root, k):
    def dfs(root):
        if not root: return
        dfs(root.right)
        if k == 0: return
        k -= 1
        if k == 0: res = root.val
        dfs(root.left)

    k = k
    dfs(root)
    return res
