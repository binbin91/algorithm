# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 不连续递增子序列的跟前0-i 个状态有关，连续递增的子序列只跟前一个状态有关
def aa(nums):
    if len(nums) == 0: return 0 
    # dp数组, 以下标i为结尾的数组的连续递增的子序列长度为dp[i]
    dp = [1] * len(nums)
    res = 1
    for i in range(len(nums)-1):
        if nums[i+1] > nums[i]: # 连续记录
            dp[i+1] = dp[i] + 1  # 递推公式
        res = max(res, dp[i+1])
    return res


if __name__ == "__main__":
    print aa([1,3,5,4,7])
