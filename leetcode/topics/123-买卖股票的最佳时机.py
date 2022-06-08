# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 最多可以完成两笔交易, 意味着可以买卖一次, 买卖两次, 也也不买卖
def aa(prices):
    # dp数组
    # 一天五个状态: 0. 没有操作 1. 第一次买入 2.第一次卖出 3.第二次买入 4.第二次卖出(奇数买入, 偶数卖出)
    # dp[i][j], 表示第i天状态j所获取最大现金
    length = len(prices)
    if length == 0: return 0
    dp = [[0] * 5 for _ in range(length)]
    # dp数组初始化
    dp[0][1] = -prices[0]
    dp[0][3] = -prices[0]
    # 递推公式
    #   dp[i][1]状态
    #     第i天买入股票, dp[i][1] = dp[i-1][0] - prices[i]
    #     第i天无操作, 沿用前一天买入状态, dp[i][1] = dp[i-1][1]
    #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    #   dp[i][2]状态
    #     第i天卖出股票, dp[i][2] = dp[i-1][1] + prices[i]
    #     第i天无操作, 沿用前一天买出状态, dp[i][2] = dp[i-1][2]
    #     dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
    #   剩余状态
    #     dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
    #     dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
    for i in range(1, length):
        dp[i][0] = dp[i-1][0] 
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) 
        dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i]) 
        dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i]) 
        dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i]) 
    return dp[-1][4]


if __name__ == "__main__":
    print aa([3, 3, 5, 0, 0, 3, 1, 4])
