# -*- coding: utf-8 -*-

# 使每个元素最多出现两次
def aa(nums):
    if len(nums) <= 2: return 2 
    f, s = 2, 2
    while f < len(nums):
        if nums[s-2] != nums[f]:
            nums[s] = nums[f]
            s += 1
        f += 1
    return s


if __name__ == "__main__":
    print aa([1,1,1,2,2,3])
    print aa([0,0,1,1,1,1,2,3,3])
