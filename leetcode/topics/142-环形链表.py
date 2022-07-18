# -*- coding: utf-8 -*-

# 双指针解法
# 知识点1, 是否有环: 快指针每次移动2个节点, 慢指针每次移动1个节点, 若相遇说明有环
# 知识点2, 环入口: 从头节点出发一个指针, 相遇节点出发一个指针, 这两个指针每次只走一个节点, 它们相遇就是环入口的节点 


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
