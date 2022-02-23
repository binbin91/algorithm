# -*- coding: utf-8 -*-


def aa(nums):
    if not nums: return 0
    j = 0
    for i in xrange(len(nums)):
        if nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums 


if __name__ == "__main__":
    print aa([0,1,0,3,12])
    print aa([0])
