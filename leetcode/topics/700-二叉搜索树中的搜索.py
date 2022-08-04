# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

# 传入根节点, 返回搜索数值所在的节点
# 若root为空 or 找到这个数值, 就返回root节点
# 因二叉搜索树是有序的, 若root.val > val就搜索左子树, 否则就搜索右子树, 都没搜索到就返回NULL

def aa(root, val):
    if not root or root.val == val: 
        return root
    if root.val > val: 
        return aa(root.left, val)
    if root.val < val: 
        return aa(root.right, val)


# 迭代法
def bb(root, val):
    while root:
        if val < root.val: 
            root = root.left
        elif val > root.val: 
            root = root.right
        else: 
            return root
    return None
