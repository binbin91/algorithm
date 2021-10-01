# -*- coding: utf-8 -*-

from ll import ListNode, LinkList


# 递增链表, 采用双指针遍历l1,l2, 根据l1.val和l2.val的大小决定添加顺序, 一直到遍历完毕 
def aa(l1, l2):
    cur = dum = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2  # 合并剩余尾部 
    return dum.next

if __name__ == "__main__":
    l1_data = [1,3,4]
    l1 = LinkList()
    for i in l1_data: l1.append(i)
    l1_head = l1.head() 

    l2_data = [1,2,4]
    l2 = LinkList()
    for i in l2_data: l2.append(i)
    l2_head = l2.head()
    a = aa(l1_head, l2_head)
    print a.val
