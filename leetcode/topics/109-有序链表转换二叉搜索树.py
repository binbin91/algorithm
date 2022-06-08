# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

def aa(head):
    if not head: return head
    pre, f, s = None, head, head
    while f and f.next:
        pre, f, s = s, f.next.next, s.next

    if pre: pre.next: None
    root = TreeNode(s.val)
    if f == s: return root
    root.left = aa(head)
    root.right = aa(s.next)
    return root
