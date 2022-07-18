# -*- coding: utf-8 -*-

# 剑指offer52题
# 双指针解法
# 根据快慢法则, 走得快的一定会追上慢的
# 有的链表短的，它走完就会去走另外一条链表, 如果有交点, 它们最终会在同一个位置相遇

def aa(headA, headB):
    p1, p2 = headA, headB
    while p1 != p2:
        # 若p1走完, 切换到p2走
        p1 = p1.next if p1 else headB
        # 若p2走完, 切换到p1走
        p2 = p2.next if p2 else headA
    return p1
