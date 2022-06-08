# -*- coding: utf-8 -*-

# 数组
# 将所有元素放入数组里, 利用双指针迭代比较元素内容
def aa(head):
    if not (head and head.next): return True
    res = []
    while head:
        res.append(head.val)
        head = head.next
    
    i, j = 0, len(res)-1
    while i < j:
        if res[i] != res[j]: return False
        i, j = i + 1, j - 1
    return True


# 快慢指针 + 反转链表
def bb(head):
    if not head.next: return True
    f, s = head, head
    while f and f.next:
        pre, f, s = s, f.next.next, s.next

    # 分割链表
    pre.next = None
    # 前半部分(c1), 反转后半部分(c2)
    c1, c2 = head, reverse(s)
    while c1:
        if c1.val != c2.val: return False
        c1, c2 = c1.next, c2.next
   return True


def reverse(head):
    cur, pre = head, None
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre
