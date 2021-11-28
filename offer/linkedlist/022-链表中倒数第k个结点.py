# -*- coding: utf-8 -*-

from ll import LinkList


# 双指针, p1优先k步, p1和p2一起往后移动, 直到p1到达链表末尾时停止 
def aa(head, k):
    if not head or k < 1:
        return None

    p1, p2 = head, head
    for _ in range(k):
        if not p1:
            return None  #越界
        p1 = p1.next
  
    while p1:
        p1, p2 = p1.next, p2.next
    return p2


if __name__ == "__main__":
    data = [1,2,3,4,5]
    k = 3
    l = LinkList()
    for i in data: l.append(i)
    head = l.get(0)
    a = aa(head, k)
    print a.val
