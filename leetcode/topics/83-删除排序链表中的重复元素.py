# -*- coding: utf-8 -*-

from ll import ListNode, LinkList



def aa(head):
    d = c = ListNode(0)
    c.next = head
    while c.next and c.next.next:
        if c.next.val == c.next.next.val:
            c.next = c.next.next
        else:
            c = c.next
    return d.next


if __name__ == "__main__":
    data = [1,1,2,2,3]
    l = LinkList()
    for i in data: l.append(i)
    head = l.get(0)
    a = aa(head)
    while a:
        print a.val
        a = a.next
