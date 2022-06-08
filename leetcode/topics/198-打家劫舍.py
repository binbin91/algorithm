# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    # dp数组, 下标i以内的房屋, 最多可以偷窃的金额为dp[i] 
    dp = [0] * len(nums) 
    # 递推公式基础是dp[0]和dp[1], 从dp[i]定义来讲, dp[0]一定是nums[0], dp[1]就是nums[0]和nums[1]最大值 
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    # 决定dp[i]的因素是偷还是不偷, 第i-1房不考虑即dp[i-1], i-2考虑偷即dp[i-2] + nums[i]
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])  # 递推公式
    return dp[-1]


if __name__ == "__main__":
    print aa([1, 2, 3, 1])
