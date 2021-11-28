# -*- coding: utf-8 -*-


# 利用辅助栈, 遍历树的所有节点, 再进行左右子节点交换
def aa(root):
    if not root: return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
        node.left, node.right = node.right, node.left
    return root

# 递归
def bb(root)
    if not root: return 
    root.left, root.right = self.bb(root.right), self.bb(root.left)
    return root
