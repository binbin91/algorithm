# -*- coding: utf-8 -*-


def aa(root, sum):
    def dfs(root, sl):
        if not root: return 0
        sl = [num + root.val for num in sl]
        sl.append(root.val)
        
        count = 0
        for n in sl:
            if n == sum: count += 1
        return count + dfs(root.left, sl) + dfs(root.right, sl)
    return dfs(root, [])
