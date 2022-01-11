# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 组合不强调顺序, 排序强调顺序
# 本题求的是排列总和
# 已知, 求装满背包有几种方法，递推公式一般都是dp[i] += dp[i - nums[j]]
def aa(nums, target):
    dp = [0] * (target + 1) 
    dp[0] = 1 # 此声明, 仅仅为了推导递推公式
    # 先遍历背包, 再内层遍历物品
    for i in range(1, target + 1):
        for j in nums:
            if i >= j:
                dp[i] += dp[i-j]  # 递推公式
    return dp[-1]


if __name__ == "__main__":
    print aa([1, 2, 3], 4)
