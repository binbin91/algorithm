# -*- coding: utf-8 -*-


# 递归版本
def aa(head):
    if not (head and head.next): return head
    tmp = head.next
    head.next = aa(tmp.next)
    tmp.next = head
    return tmp


# 迭代版本
def bb(head):
    res = ListNode(next=head)
    pre = res
    # pre必须有下一个和下下个才能交换
    while pre.next and pre.next.next:
        cur = pre.next
        post = pre.next.next
        # pre, cur, post对应最左, 中间的, 最右边的节点
        cur.next = post.next
        post.next = cur
        pre.next = post
        pre = pre.next.next
    return res.next
