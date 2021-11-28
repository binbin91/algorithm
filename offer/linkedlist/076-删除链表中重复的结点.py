# -*- coding: utf-8 -*-

from ll import LinkList, ListNode


def aa(head):
    pre = ListNode(0)
    pre.next = head
    
    cur, p = head, pre
    while cur and cur.next:
        if cur.val != cur.next.val:
            cur, p = cur.next, p.next
        else:
            val = cur.val
            while cur and cur.val == val:
                cur = cur.next
            p.next = cur

    return pre.next


if __name__ == "__main__":
    data = [1,2,3,3,4,4,5]
    l = LinkList()
    for i in data: l.append(i)
    head = l.get(0) 
    a = aa(head)
    while a != None:
        print a.val
        a = a.next
