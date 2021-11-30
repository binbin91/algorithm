# -*- coding: utf-8 -*-


def aa(p, q):
    if not p and not q: return True
    if not p or not q or p.val != q.val: return False
    return aa(l.left, r.left) and aa(l.right, r.right)
