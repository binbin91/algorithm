# -*- coding: utf-8 -*-

def aa(l1, l2):
    res = node = ListNode(0)
    remaining = 0
    while l1 or l2:
        if not l1: node.next, l1 = l2, ListNode(0)
        if not l2: node.next, l2 = l1, ListNode(0)
        remaining += l1.val + l2.val
        node.next = ListNode(remaining % 10)
        remaining = remaining // 10
        node = node.next
        l1, l2 = l1.next, l2.next
    if remaining: node.next = ListNode(remaining) 
    return res.next 
