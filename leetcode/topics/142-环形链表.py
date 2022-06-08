# -*- coding: utf-8 -*-

def aa(head):
    fast, slow = head, head
    while True:
       if not (fast and fast.next): return
       fast, slow = fast.next.next, slow.next
       if fast == slow: break
    
    fast = head
    while fast != slow:
        fast, slow = fast.next, slow.next
    return slow
