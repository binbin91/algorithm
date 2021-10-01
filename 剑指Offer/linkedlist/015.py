# -*- coding: utf-8 -*-

from ll import LinkList


# 双指针
def aa(head):
    cur, pre = head, None
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre 


if __name__ == "__main__":
    data = [1,2,3]
    l = LinkList()
    for i in data: l.append(i)
    head = l.head()
    a = aa(head)
    print a.val
