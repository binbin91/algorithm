# -*- coding: utf-8 -*-

# 贪心
def aa(nums):
    res = 0
    if len(nums) == 1: return True
    i = 0
    while i <= res:
        res = max(res, i + nums[i])
        if res >= len(nums) - 1: return True
        i += 1
    return False


# dp
def bb(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        if dp[i-1] >= i:
            dp[i] = max(dp[i-1], i+nums[i])
        else:
            dp[i] = dp[i-1]
    return dp[i-1]>=len(nums)-1


def cc(nums):
    max_len = nums[0]
    for i in range(1, len(nums)):
        if max_len >= i: max_len = max(max_len, i + nums[i])
    return max_len >= len(nums)-1


if __name__ == "__main__":
    print cc([2,3,1,1,4])
    print cc([3,2,1,0,4])
