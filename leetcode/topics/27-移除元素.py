# -*- coding: utf-8 -*-

def aa(nums, val):
    f = s = 0
    while f < len(nums):
        if nums[f] != val:
            nums[s] = nums[f]
            s += 1
        f += 1
    return s


if __name__ == "__main__":
    print aa([3,2,2,3], 3)
    print aa([0,1,2,2,3,0,4,2], 2)
