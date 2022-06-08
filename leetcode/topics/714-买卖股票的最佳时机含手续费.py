# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 买卖多次，每次有手续费
def aa(prices, fee):
    # dp数组, dp[i][0]表示第i天持有股票所得最多现金, dp[i][1]表示第i天不持有股票所得最多现金 
    length = len(prices)
    if length == 0: return 0
    dp = [[0] * 2 for _ in range(length)]
    # dp数组初始化
    dp[0][0] = -prices[0]
    # 递推公式
    # 第i天持有股票所得最多现金
    #   第i-1天就持有股票, 保持现状即所得现金就是昨天持有股票的所得现金, dp[i-1][0]
    #   第i天买入股票, 所得现金就是昨天不持有股票的所得现金减去今天的股票价格, dp[i-1][1] - prices[i]
    #   那么dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
    # 第i天不持有股票所得最多现金
    #   第i-1天不持有股票, 保持现状即所得现金就是昨天不持有股票的所得现金, dp[i-1][1]
    #   第i天卖出股票, 所得现金就是按照今天股票价格卖出后所得现金再减去手续费, dp[i-1][0] + prices[i] - fee
    #   那么dp[i][0] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
    for i in range(1, length):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee) 
    return max(dp[-1][0], dp[-1][1])


if __name__ == "__main__":
    print aa([1, 3, 2, 8, 4, 9], 2)
