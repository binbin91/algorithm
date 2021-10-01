# -*- coding: utf-8 -*-


# 双指针
def aa(head):
    fast, slow = head, head
    while True:
        if not (fast and fast.next): return
        fast, slow = fast.next.next, slow.next
        if fast == slow: break   # 第一次相遇

    fast = head
    while fast != slow:  # 从遇见点和头部出发,必然找到入口
        fast, slow = fast.next, slow.next
    return slow
