# -*- coding: utf-8 -*-


def isSubtree(s, t):
    if not s and not t: return True
    if not s or not t: return False
    return aa(s, t) or isSubtree(s.left, t) or isSubtree(s.right, t)


def aa(p, q):
    if not p and not q: return True
    if not p or not q or p.val != q.val: return False
    return aa(l.left, r.left) and aa(l.right, r.right)
