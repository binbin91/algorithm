# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 普通二叉树求最近公共祖先需要回溯, 自底向上查找, 而二叉搜索树有序(自带方向), 只需要从上向下遍历即可

# 传递当前节点 & p & q, 返回最近公共祖先
# 遇到空节点返回即可
# 若root > p and root > q, 那么应该向左遍历, 反之亦然

def aa(root, p, q):
    if root.val > p.val and root.val > q.val:
        return aa(root.left, p, q)
    if root.val < p.val and root.val < q.val: 
        return aa(root.right, p, q)
    return root


# 迭代法
def bb(root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
