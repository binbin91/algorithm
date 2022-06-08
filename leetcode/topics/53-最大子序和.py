# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(nums):
    if len(nums) == 0: return 0
    # dp数组, 包括下标i之前的最大连续子序列和为dp[i]
    dp = [0] * len(nums)
    res = dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])  # 递推公式
        res = max(res, dp[i]) # 保存dp[i]最大值
    return res


if __name__ == "__main__":
    print aa([-2,1,-3,4,-1,2,1,-5,4])
