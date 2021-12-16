# -*- coding: utf-8 -*-


def aa(head):
    s = f = head
    while f.next:
        f, s = f.next.next, s.next
    return s
