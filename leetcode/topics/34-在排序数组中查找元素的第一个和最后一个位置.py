# -*- coding: utf-8 -*-

# 二分法
# 寻找target在数组的左右边界, 有如下3种情况:
# 1. target在数组范围的右or左, 例如[3,4,5], target为2 或者target为6, 此时返回[-1,-1]
# 2. target在数组范围中, 且数组不存在target, 例如[3,6,7], target为5, 此时返回[-1,-1]
# 3. target在数组范围中, 且数组中存在target, 例如[3,6,7], target为6, 此时返回[1, 1]
# 考虑这3种情况后，采用二分法左右边界
# 右边界: if nums[m] > target: r = m - 1, l = m + 1; else: rightBorder = l
# 左边界: if nums[m] >= target, r = m - 1, leftBorder = r; else: l = m + 1

# 从解法1开始理解, 便于掌握
def aa(nums, target):
    def left_border(nums, target):
        l, r, lb = 0, len(nums)-1, -1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m - 1
                lb = r
            else:
                l = m + 1
        return lb

    def right_border(nums, target):
        l, r, rb = 0, len(nums)-1, -2
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
                rb = l
        return rb

    lb = left_border(nums, target)
    rb = right_border(nums, target)
    # 情况一
    if lb == -2 or rb == -2: return [-1, -1] 
    # 情况三
    if rb - lb > 1: return [lb+1, rb-1]
    # 情况二
    return [-1, -1]


def bb(nums, target):
    def bs(nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r -l) // 2
            if nums[m] > target: r = m - 1
            elif nums[m] < target: l = m + 1
            else: return m
        return -1
    
    index = bs(nums, target)
    # nums中不存在target, 直接返回[-1, -1]
    if index == -1: return [-1, -1]
    # nums中存在target, 则左右滑动指针, 找到符合题意区间
    l, r = index, index
    # 向左滑动, 找左边界
    while l-1 >= 0 and nums[l-1] == target: l -= 1
    # 向右滑动, 找右边界
    while r+1 < len(nums) and nums[r+1] == target: r += 1
    return [l, r]
            


if __name__ == "__main__":
    print aa([5,7,7,8,8,10], 8)
    print aa([5,7,7,8,8,10], 6)
    print aa([], 0)
