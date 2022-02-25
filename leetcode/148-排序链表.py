# -*- coding: utf-8 -*-


def aa(head):
    if not head or not head.next: return head
    # 快慢指针, 找到中间点
    f, s = head.next, head
    while f and f.next:
        f, s = f.next.next, s.next
    m, s.next = s.next, None
    # 归并排序
    l1, l2 = aa(head), aa(m)
    return merged(l1, l2)

# JZ025 合并有序链表
def merged(l1, l2):
    res = node = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            node.next, l1 = l1, l1.next
        else:
            node.next, l2 = l2, l2.next
        node = node.next
    node.next = l1 if l1 else l2
    return res.next
