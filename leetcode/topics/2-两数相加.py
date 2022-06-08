# -*- coding: utf-8 -*-

# 面试题02-05链表求和
def aa(l1, l2):
    res = node = ListNode(0)
    r = 0
    while l1 or l2:
        if not l1: node.next, l1 = l2, ListNode(0)
        if not l2: node.next, l2 = l1, ListNode(0)
        r += l1.val + l2.val
        node.next = ListNode(r % 10)
        r = r // 10
        node = node.next
        l1, l2 = l1.next, l2.next
    if r: node.next = ListNode(r)
    return res.next
