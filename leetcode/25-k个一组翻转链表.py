# -*- coding: utf-8 -*-

def aa(head, k):
    p = res = ListNode(0)
    while True:
    	count, stack, tmp = k, [], head
        while count and tmp:
            stack.append(tmp)
            tmp = tmp.next
            count -= 1
        if count:
            p.next = head
            break
        while stack:
            p.next = stack.pop()
            p = p.next
        p.next, head = tmp, tmp
    return res.next
