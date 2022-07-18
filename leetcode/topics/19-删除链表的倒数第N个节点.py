# -*- coding: utf-8 -*-

# 某次面试, 遇到过这题, 强烈建议掌握解法
# 双指针解法
# fast先移动n步, fast和slow一起移动, 直到fast到链表末尾, 删除slow指向的节点即可


def aa(head, n):
    node = ListNode(0, head)
    s = f = node
    # fast先移动n步
    for _ in range(n):
        f = f.next
    
    while f.next:
        f, s  = f.next, s.next
    # fast走到链表末尾, slow下一个节点为倒数第N个节点, 将其删除即可
    s.next = s.next.next
    return node.next


if __name__ == "__main__":
    data = [1,2,3,4,5]
    n = 2
    l = LinkList()
    for i in data: l.append(i)
    head = l.head()
    a = aa(head, n)
    while a:
        print a.val
        a = a.next
