# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(nums, target):
    sv = sum(nums)
    if target > sv or (sv + target) % 2 == 1: return 0
    bs = (sv + target) // 2
    dp = [0] * (bs + 1)
    dp[0] = 1
    for i in range(len(nums)):
        for j in range(bs, nums[i]-1, -1):
            dp[j] += dp[j-nums[i]]  # 递推公式
    return dp[bs]


if __name__ == "__main__":
    print aa([1,1,1,1,1], 3)
