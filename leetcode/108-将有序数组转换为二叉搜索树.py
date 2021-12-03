# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

def aa(nums):
    def recur(nums, l, r):
        if l > r: return
        m = l + (r-l) // 2
        m_r = TreeNode(nums[m])
        m_r.left = recur(nums, l, m-1)
        m_r.right = recur(nums, m+1, r)
        return m_r
    return recur(nums, 0, len(nums)-1) 
