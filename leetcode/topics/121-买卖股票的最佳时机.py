# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 只能买卖一次
def aa(prices):
    # dp数组, dp[i][0]表示第i天持有股票所得最多现金, dp[i][1]表示第i天不持有股票所得最多现金 
    length = len(prices)
    if length == 0: return 0
    dp = [[0] * 2 for _ in range(length)]
    # dp数组初始化
    # 递推公式基于dp[0][0]和dp[0][1]
    # dp[0][0]为第0天持有股票(买入股票), 即dp[0][0] -= prices[0]
    # dp[0][1]为第0天不持有股票, 即dp[0][1] -= 0
    dp[0][0] = -prices[0]
    dp[0][1] = 0
    # 递推公式
    # 第i天持有股票所得最多现金
    #   第i-1天就持有股票, 保持现状即所得现金就是昨天持有股票的所得现金, dp[i-1][0]
    #   第i天买入股票, 所得现金就是买入今天股票后所得现金, -prices[i]
    #   那么dp[i][0] = max(dp[i-1][0], -prices[i])
    # 第i天不持有股票所得最多现金
    #   第i-1天不持有股票, 保持现状即所得现金就是昨天不持有股票的所得现金, dp[i-1][1]
    #   第i天卖入股票, 所得现金就是按照今天股票卖出后所得现金, dp[i-1][0] + prices[i]
    #   那么dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
    for i in range(1, length):
        dp[i][0] = max(dp[i-1][0], -prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
    return dp[-1][1]


if __name__ == "__main__":
    print aa([7, 1, 5, 3, 6, 4])
