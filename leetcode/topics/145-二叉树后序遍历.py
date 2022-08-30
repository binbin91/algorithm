# -*- coding: utf-8 -*-


# 递归
def aa(root):
    res = []
    def recur(root):
        if not root: return
        recur(root.left)
        recur(root.right)
        res.append(root.val)
    recur(root)
    return res


# 迭代
def bb(root):
    if not root: return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)    # 根先处理
        if node.left:
            stack.append(node.left)  # 左先入栈, 后出
        if node.right:
            stack.append(node.right)  # 右后入栈, 先出
    return res[::-1] # 数组翻转
