# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(nums):
    if len(nums) <= 1: return len(nums)
    # dp数组, dp[i]表示i之前包含i的最长上升子序列长度 
    dp = [1] * len(nums)
    res = 0
    # 位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1的最大值
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)  # 递推公式
        res = max(res, dp[i])
    return res


if __name__ == "__main__":
    print aa([10,9,2,5,3,7,101,18])
