# -*- coding: utf-8 -*-

# 解体思路:
#   采用双指针解法
#   起始位置和终止比较平方的大小, 大的存入新数组并移动指针, 小的停留原地

def aa(nums):
    i, j, k, n = 0, len(nums)-1, len(nums)-1, len(nums)
    ans = [-1] * n
    while i <= j:
        lm = nums[i] ** 2
        rm = nums[j] ** 2 
        if lm > rm:
            ans[k] = lm
            i += 1
        else:
            ans[k] = rm
            j -= 1
        k -= 1
    return ans


if __name__ == "__main__":
    print aa([-4,-1,0,3,10])
    print aa([-7,-3,2,3,11])
