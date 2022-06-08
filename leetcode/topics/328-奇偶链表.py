# -*- coding: utf-8 -*-

from ll import LinkList


def aa(head):
    if not head: return head
    odd = head
    even_head = even = head.next
    while odd.next and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
    odd.next = even_head
    return head    


if __name__ == "__main__":
    data = [1,2,3,4,5]
    l = LinkList()
    for i in data: l.append(i)
    head = l.get(0)
    a = aa(head)
    while a:
        print a.val
        a = a.next
