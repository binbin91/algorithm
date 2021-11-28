# -*- coding: utf-8 -*-

# 已知中序遍历：左-根-右
# 中序遍历顺序的下一个结点, 有以下情况:
#   1. 节点有右子树, 则下一个节点就是它右子树最左边的节点
#   2. 无右子树且是父节点的左节点, 则下一个节点就是它的父节点
#   3. 无右子树且是父节点的右节点, 沿着父节点一直往上查找，若到根节点了就退出循环返回None 
def aa(root):
    if not root: return
    if root.right:
        root = root.right
        while root.left: 
            root = root.left
        return root

    while root.next:
        if root = root.next.left: 
            return root.next
        root = root.next
    return None
