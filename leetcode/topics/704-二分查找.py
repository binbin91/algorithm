# -*- coding: utf-8 -*-

def aa(nums, target):
    i, j = 0, len(nums)
    while i < j:
        m = (i + j) / 2
        if nums[m] < target: i = m + 1 
        elif nums[m] > target: j = m
        else: return m
    return -1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    print aa(nums, 9)
    print aa(nums, 2)
