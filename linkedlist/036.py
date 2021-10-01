# -*- coding: utf-8 -*-


# 双指针浪漫相遇
def aa(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
