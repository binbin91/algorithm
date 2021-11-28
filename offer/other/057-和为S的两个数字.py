# -*- coding: utf-8 -*-

def aa(nums, target):
    i,j = 0, len(nums)-1
    while i < j:
        s = nums[i] + nums[j]
        if s > target: j -= 1
        elif s < target: i += 1
        else: return nums[i], nums[j]
    return '' 


if __name__ == "__main__":
    print aa([2,7,11,15], 9)
