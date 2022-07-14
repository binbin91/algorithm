# -*- coding: utf-8 -*-

# 解体思路:
#   题目数组是有序数组，且无重复元素，故使用二分查找法
#   二分查找边界条件, 选择左闭右开(不包含右区间)
#   right赋值: 左闭右闭right = len(nums)-1, 左闭右开right = len(nums)
#   若nums[mid] > target, 那下一个搜索左区间是不包含nums[mid]对应数值, 所以right = mid
#   若nums[mid] < target, mid不是target, 那下一个搜索区间是不能包含这个mid, 所以left = mid + 1  


def aa(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    print aa(nums, 9)
    print aa(nums, 2)
