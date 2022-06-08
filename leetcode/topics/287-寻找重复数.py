# -*- coding: utf-8 -*-


# 快慢指针
def aa(nums):
    s = f = 0
    while True:
        f, s = nums[nums[f]], nums[s]
        if f == s: break

    s = 0
    while f != s: 
        f, s = nums[f], nums[s]
    return s


if __name__ == "__main__":
    print aa([1,3,4,2,2])
    print aa([3,1,3,4,2])
