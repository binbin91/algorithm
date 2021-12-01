# -*- coding: utf-8 -*-


def aa(nums):
    if not nums: return

    v = max(nums)
    idx = nums.index(v)
    root = TreeNode(v)
    l, r = nums[:idx], nums[idx+1:]
    root.left = aa(left)
    root.right = aa(right)
    return root
