# -*- coding: utf-8 -*-

# 高阶要求, 使用空间复杂度O(1)原地算法解答本题
# 本题和剑指第58题左旋字符串很像, 剑指是左旋, 本题是右旋
# 参照左旋解法, 就是将反转顺序改动一下, 步骤如下:
#  1. 反转整个字符串
#  2. 反转区间为前k的子串
#  3. 反转区间为k到末尾的子串 

def aa(nums, k):
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    n = len(nums)
    k %= n 
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)
    return nums


if __name__ == "__main__":
    print aa([1,2,3,4,5,6,7], 3)
    print aa([-1,-100,3,99], 2)
