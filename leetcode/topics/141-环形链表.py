# -*- coding: utf-8 -*-


def aa(head):
    if not head: return False
    fast, slow = head, head
    while fast and fast.next:
       fast, slow = fast.next.next, slow.next
       if fast == slow:
           return True
    return False 
