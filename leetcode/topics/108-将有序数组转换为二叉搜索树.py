# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

# 根据数组构造二叉树, 本质就是寻找分割点, 通过分割点作为当前节点, 来递归左区间和右区间
# 因有序数组构造二叉树, 分割点就是数组中间位置节点
# 当left > right时返回即可
# 获取数组元素中间位置, 接着划分区间, root的左孩子接住下一层左区间的构造节点，右孩子接住下一层右区间构造的节点

def aa(nums):
    def recur(nums, left, right):
        if left > right: return
        mid = left + (right-left) // 2
        m_r = TreeNode(nums[mid])
        m_r.left = recur(nums, left, mid-1)
        m_r.right = recur(nums, mid+1, right)
        return m_r
    return recur(nums, 0, len(nums)-1) 
