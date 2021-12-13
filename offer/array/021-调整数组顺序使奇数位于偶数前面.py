# -*- coding: utf-8 -*-


def aa(nums):
    i, j = 0, len(nums) - 1
    while i < j:
        while i < j and nums[i] & 1 == 1: i += 1
        while i < j and nums[j] & 1 == 0: j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == "__main__":
    array = [1,2,3,4]
    print reOrderArray(array)
