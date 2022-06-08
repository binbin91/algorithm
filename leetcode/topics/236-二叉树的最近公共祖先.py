# -*- coding: utf-8 -*-


def aa(root, p, q):
    if not root or root == p or root == q: return root 
    left = aa(root.left, p, q)
    right = aa(root.right, p, q)
    if not left: return right
    if not right: return left
    return root
