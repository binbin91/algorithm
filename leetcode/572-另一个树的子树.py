# -*- coding: utf-8 -*-

def aa(p, q):
    if not p and not q: return True
    if not p or not q: return False
    return aa(l.left, r.left) and aa(l.right, r.right)

def isSubtree(s, t):
    if not s and not t: return True
    if not s or not t: return False
    return aa(s, t) or isSubtree(s.left, t) or isSubtree(s.right, t)
