# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 自底向上查找, 就可以找到公共祖先, 采用后序遍历(天然回溯, 从底往上), 最先处理的一定是叶子节点

# 递归函数返回值，需要告知是否找到节点p or 节点q, 那么返回返回值bool类型即可
# 找到节点p or 节点q or 空节点, 就返回
# 遍历整棵树, 若left和right不为空, root就是最近公共节点, 若left为空right不为空就返回right, 反之亦然

def aa(root, p, q):
    if not root or root == p or root == q: return root 
    left = aa(root.left, p, q)
    right = aa(root.right, p, q)
    if not left: return right
    if not right: return left
    return root
