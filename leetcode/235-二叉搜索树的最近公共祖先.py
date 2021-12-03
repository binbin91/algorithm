# -*- coding: utf-8 -*-


def aa(root, p, q):
    if root.val > p.val and root.val > q.val:
        return aa(root.left, p, q)
    if root.val < p.val and root.val < q.val: 
        return aa(root.right, p, q)
    return root
