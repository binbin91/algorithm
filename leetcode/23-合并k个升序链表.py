# -*- coding: utf-8 -*-


def aa(lists):
    if not head: return
    n = len(lists)
    return merge(lists, 0, n - 1)

def merge(lists, l, r):
    if l == r: return lists[l]
    m = l + (r - l) // 2
    l1 = merge(lists, l, m)
    l2 = merge(lists, m+1, r)
    return mt(l1, l2)

def mt(l1, l2):
    if not l1: return l2
    if not l2: return l1
    if l1.val < l2.val:
        l1.next = mt(l1.next, l2)
        return l1
    else:
        l2.next = mt(l1, l2.next)
        return l2
