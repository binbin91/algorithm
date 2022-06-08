# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(coins, amount):
    # dp数组, 凑成总金额j所需货币的最少个数为dp[j]
    dp = [amount + 1] * (amount + 1) 
    # dp数组初始化, 凑成总金额0的货币组合数为1
    dp[0] = 0
    # 先遍历物品(钱币),再遍历背包(总金额)
    # 本题求钱币最小个数(完全背包), 两种for循环都不会影响最终结果
    for i in coins:
        for j in range(i, amount+1):
            # 递推公式
            # 得到dp[j], 只有一个来源dp[j - coins[i]]
            # 凑足金额j - coins[i]的最少个数为dp[j - coins[i]], 那么只需加上coins[i] 即dp[j - coins[i]] + 1
            # 所以dp[j]要取所有dp[j - coins[i]] + 1中最小的，即dp[j] = min(dp[j-coins[i]] + 1, dp[j])
            dp[j] = min(dp[j], dp[j-i] + 1)
    return dp[amount] if dp[amount] < amount + 1 else -1


if __name__ == "__main__":
    print aa([1, 2, 5], 5)
