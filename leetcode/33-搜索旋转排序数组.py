# -*- coding: utf-8 -*-

# 要求O(log n) -> 二分法
# 1. 找出mid, 通过mid判断是在有序部分还是无序部分
#    有序判断: mid < left, mid右边是有序
#    无序判断: mid >= left, mid左边是有序
# 2. 判断target在那一边, 就可以舍弃另一边
#    例: mid在右侧有序, 只需判断mid <= target <= end, 就知道target在右侧有序部分, 就可以舍弃左边部分(l = m + 1)
def aa(nums, target):
    n = len(nums)
    if n == 0: return -1
    l, r = 0, n - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        # 若中间值大于左边值, 说明左边有序
        if nums[m] > nums[l]:
            if nums[l] <= target <= nums[m]:
                r = m
            else:
                l = m + 1
        # 反过来则右边有序
        else:
            if nums[m+1] <= target <= nums[r]:
                l = m + 1
            else:
                r = m
    return l if nums[l] == target else -1
            


if __name__ == "__main__":
    print aa([4,5,6,7,0,1,2], 0)
    print aa([4,5,6,7,0,1,2], 3)
    print aa([1], 0)
