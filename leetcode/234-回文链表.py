# -*- coding: utf-8 -*-

def aa(head):
    if not (head and head.next): return True
    p = ListNode(0)
    p.next, s, f = head, p, p
    while f and f.next:
        f, s = f.next.next, s.next
    cur, pre, s.next = s.next, None, None 
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    a, b = p.next, pre
    while b:
        if a.val != b.val: return False
        a, b = a.next, b.next
    return True
