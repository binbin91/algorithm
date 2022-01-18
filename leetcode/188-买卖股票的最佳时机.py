# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 最多买卖k次
def aa(k, prices):
    # dp数组
    # 一天k个状态: 0. 没有操作 1. 第一次买入 2.第一次卖出 3.第二次买入 4.第二次卖出...(奇数买入, 偶数卖出)
    # dp[i][j], 表示第i天状态j所获取最大现金
    length = len(prices)
    if length == 0: return 0
    dp = [[0] * (2 * k + 1) for _ in range(length)]
    # dp数组初始化, 买入即现金减少，推导出当i为奇数都初始化为-prices[0]
    for i in range(1, 2*k, 2):
        dp[0][i] = -prices[0]
    # 递推公式
    #   dp[i][1]状态
    #     第i天买入股票, dp[i][1] = dp[i-1][0] - prices[i]
    #     第i天无操作, 沿用前一天买入状态, dp[i][1] = dp[i-1][1]
    #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    #   dp[i][2]状态
    #     第i天卖出股票, dp[i][2] = dp[i-1][1] + prices[i]
    #     第i天无操作, 沿用前一天买出状态, dp[i][2] = dp[i-1][2]
    #     dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
    for i in range(1, length):
        for j in range(0, 2*k-1, 2):
            dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i]) 
            dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i]) 
    return dp[-1][2*k]


if __name__ == "__main__":
    print aa(2, [2, 4, 1])
