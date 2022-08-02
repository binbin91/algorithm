# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 传入存放元素的数组, 返回该数组构造的二叉树根节点
# 空数组返回
# 先找到数组中最大值和对应下标, 构造根节点, 利用下标来分割数组, 最大值所在下标左区间构造左子树, 下标右区间构造右子树

def aa(nums):
    if not nums: return
    v = max(nums)
    idx = nums.index(v)
    root = TreeNode(v)
    left, right = nums[:idx], nums[idx+1:]
    root.left = aa(left)
    root.right = aa(right)
    return root
