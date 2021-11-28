# -*- coding: utf-8 -*-

def aa(head):
    if not (head and head.next): return head
    tmp = head.next
    head.next = aa(tmp.next)
    tmp.next = head
    return tmp
