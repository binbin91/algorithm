# -*- coding: utf-8 -*-

def aa(head, val):
    node = ListNode(0, head)
    cur = node
    while cur.next:
        if cur.next.val == val: 
            cur.next = cur.next.next
        else:
            cur = cur.next
    return node.next 
