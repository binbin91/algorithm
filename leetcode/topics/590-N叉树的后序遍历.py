# -*- coding: utf-8 -*-


def aa(root):
    if not root: return []
    res, queue = [], [root]
    while queue: 
        node = queue.pop()
        res.append(node.val)
        queue.extend(node.children)
    return res[::-1]
