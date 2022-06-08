# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(nums):
    target = sum(nums)
    if target % 2 == 1: return False
    target //= 2
    dp = [0] * 10001
    for i in range(len(nums)):
        for j in range(target, nums[i]-1, -1):
            dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])  # 递推公式
    return target == dp[target]


if __name__ == "__main__":
    print aa([1,5,11,5])
    print aa([1,2,3,5])
