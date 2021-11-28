# -*- coding: utf-8 -*-

from ll import LinkList


def aa(head, val):
    if head.val == val: return head.next
    pre, cur = head, head.next
    while cur and cur.val != val:
        pre, cur = cur, cur.next
    if cur: pre.next = cur.next
    return head

if __name__ == "__main__":
    data = [1,4,2,4]
    l = LinkList()
    for i in data: l.append(i)
    head = l.get(0)
    hn = aa(head, 1)
    while hn:
        print hn.val
        hn = hn.next
