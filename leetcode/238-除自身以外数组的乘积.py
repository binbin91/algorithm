# -*- coding: utf-8 -*-


def aa(nums):
    res, p, q = [1], 1, 1
    for i in range(len(nums)-1):
        p *= nums[i]
        res.append(p)

    for i in range(len(nums)-1, 0, -1):
        q *= nums[i]
        res[i-1] *= q
    return res 


if __name__ == "__main__":
    print aa([1,2,3,4])
    print aa([-1,1,0,-3,3])
