# -*- coding: utf-8 -*-


def aa(head, val):
    node = ListNode(0, head)   # 添加一个虚拟节点, 下一跳指向head
    cur = node
    while cur.next:
        if cur.next.val == val: 
            cur.next = cur.next.next  # 删除cur.next节点
        else:
            cur = cur.next
    return node.next 
