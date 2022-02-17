# -*- coding: utf-8 -*-


class Soluction(object):
    def aa(self, root):
        self.ms = float("-inf")
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ms = max(self.ms, left + right + root.val)
            return max(0, max(left, right) + root.val) 
        dfs(root)
        return self.ms
