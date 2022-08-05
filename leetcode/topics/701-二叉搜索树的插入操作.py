# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

# 传入根节点, 返回更新后的以当前root为根节点的新树
# 遇到空节点, 就是要插入节点的位置, 把要插入的节点返回即可
# 因二叉搜索树特性, 根据插入元素数组, 决定递归方向

def aa(root, val):
    if not root: return TreeNode(val)
    if val < root.val: root.left = aa(root.left, val)
    if root.val > val: root.right = aa(root.right, val)
    return root


# 迭代法
def bb(root, val):
    if not root: return TreeNode(val)

    # 遍历过程中，记录当前遍历的节点的父节点
    pre, cur = None, root
    while cur:
        if cur.val < val: 
            pre, cur = cur, cur.right
        elif cur.val > val: 
            pre, cur = cur, cur.left

    # 新节点父节点已找到, 此时把新节点插入即可
    if pre.val > val: 
        pre.left = TreeNode(val)
    else: 
        pre.right = TreeNode(val) 
    return root
