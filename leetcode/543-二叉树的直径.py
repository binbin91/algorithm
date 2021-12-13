# -*- coding: utf-8 -*-

from collections import deque


def aa(root):
    res = 1
    def recur(root):
        if not root: return 0
        left = recur(root.left)
        right = recur(root.right)
        res = max(res, left + right + 1)
        return max(left + right) + 1
    recur(root)
    return res - 1 

def bb(root):
    res, stack, queue = 0, [root], deque()
    while stack:
        node = stack.pop(0)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
        queue.appendleft(node)
 
    for i in queue:
        l = i.left.val if i.left else 0
        r = i.right.val if i.right else 0
        res = max(res, l + r)
        i.val = max(l, r) + 1
    return res
