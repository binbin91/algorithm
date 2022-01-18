# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 买卖多次, 卖出有一天冷冻期 
def aa(prices):
    # dp数组, dp[i][j], 表示第i天状态j所获取最大现金
    # 状态: 0持有股票后的最多现金 1不持有股票(能购买)的最多现金 2不持有股票(冷冻期)的最多现金
    length = len(prices)
    if length == 0: return 0
    dp = [[0] * 3 for _ in range(length)]
    # dp数组初始化
    dp[0][0] = -prices[0]
    # 递推公式
    #   dp[i][0]状态
    #     前一天持有股票状态, dp[i][0] = dp[i-1][0]
    #     今天买入, 前一天保持卖出股票状态, dp[i-1][1] - prices[i]
    #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i]))
    #   dp[i][1]状态
    #     前一天卖出股票且度过冷冻期, dp[i-1][1]
    #     前一天是冷冻期, dp[i-1][2] 
    #     dp[i][1] = max(dp[i-1][1], dp[i-1][2])
    #   dp[i][2]状态
    #     昨天买入, 今天卖出, dp[i-1][0] + prices[i]
    for i in range(1, length):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][2])
        dp[i][2] = dp[i-1][0] + prices[i]
    return max(dp[length-1][2], dp[length-1][1])


if __name__ == "__main__":
    print aa([1, 2, 3, 0, 2])
