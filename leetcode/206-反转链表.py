# -*- coding: utf-8 -*-

def aa(head):
    cur, pre = head, None
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre
