# -*- coding: utf-8 -*-

def aa(root):
    def dfs(cur):
        if not cur: return
        dfs(cur.left)
        if pre: pre.right, cur.left = cur, pre
        else: head = cur
        pre = cur
        dfs(cur.right)
       
    if not root: return
    pre = None
    dfs(root)
    head.left, pre.right = pre, head
    return head
