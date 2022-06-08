# -*- coding: utf-8 -*-

def aa(nums):
    if not nums: return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i+1


if __name__ == "__main__":
    print aa([1,1,2])
    print aa([0,0,1,1,1,2,2,3,3,4])
