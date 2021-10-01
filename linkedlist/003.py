# -*- coding: utf-8 -*-

import collections
from ll import LinkList


# 栈(后进先出), 从头到尾遍历一次链表, 使用栈来存储; 出栈的时候，得到就是链表每个节点从尾到头的顺序
def aa(head):
    res = collections.deque()
    while head:
        res.appendleft(head.val)
        head = head.next
    return list(res)

# 列表反转
def bb(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res[::-1]

if __name__ == "__main__":
    data = [1,3,2]
    l = LinkList()
    for i in data: l.append(i)
    head = l.head()
    print bb(head)
