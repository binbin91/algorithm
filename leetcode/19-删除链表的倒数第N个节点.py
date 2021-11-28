# -*- coding: utf-8 -*-

from ll import LinkList, ListNode


def aa(head, n):
    node = ListNode(0, head)
    s = f = node
    for _ in range(n):
        f = f.next
    
    while f.next:
        f, s  = f.next, s.next
    s.next = s.next.next
    return node.next


if __name__ == "__main__":
    data = [1,2,3,4,5]
    n = 2
    l = LinkList()
    for i in data: l.append(i)
    head = l.head()
    a = aa(head, n)
    while a:
        print a.val
        a = a.next
