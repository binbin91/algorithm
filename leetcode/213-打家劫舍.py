# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组


def rob(nums):
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]
    res1 = aa(nums, 0, n - 2)
    res2 = aa(nums, 1, n - 1)
    return max(res1, res2)

def aa(nums, start, end):
    if end == start: return nums[start]
    # dp数组, 下标i以内的房屋, 最多可以偷窃的金额为dp[i] 
    dp = [0] * len(nums) 
    # 递推公式基础是dp[0]和dp[1], 从dp[i]定义来讲, dp[0]一定是nums[0], dp[1]就是nums[0]和nums[1]最大值 
    dp[start] = nums[start]
    dp[start + 1] = max(nums[start], nums[start + 1])
    # 决定dp[i]的因素是偷还是不偷, 第i-1房不考虑即dp[i-1], i-2考虑偷即dp[i-2] + nums[i]
    for i in range(start + 2, end + 1):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])  # 递推公式
    return dp[end]


if __name__ == "__main__":
    print rob([2, 3, 2])
