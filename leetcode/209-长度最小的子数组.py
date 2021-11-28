# -*- coding: utf-8 -*-

def aa(s, nums):
    res, sum, index = float("inf"), 0, 0
    for i in range(len(nums)):
        sum += nums[i]
        while sum >= s:
            res = min(res, i-index+1)
            sum -= nums[index]
            index += 1
    return 0 if res == float("inf") else res 


if __name__ == "__main__":
    print aa(7, [2,3,1,2,4,3])
