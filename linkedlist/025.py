# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


def aa(head):
    if not haed: return

    # 1. 拼接链表
    cur = head
    while cur:
        tmp = Node(cur.val)
        tmp.next = cur.next
        cur.next = tmp
        cur = tmp.next

    # 2. 复制random 
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    # 3. 拆分链表
    cur = res = head.next
    pre = head
    while cur.next
        pre.next = pre.next.next
        cur.next = cur.next.next
        pre = pre.next
        cur = cur.next
    pre.next = None
    return res 
