# -*- coding: utf-8 -*-

def aa(amount, coins):
    # dp数组, 凑成总金额j货币组合数为dp[j]
    dp = [0] * (amount + 1) 
    # dp数组初始化, 凑成总金额0的货币组合数为1
    dp[0] = 1
    # 先遍历物品(钱币),再遍历背包(总金额)
    # 本题求组合数, 外层for循环遍历物品, 内层遍历背包
    # 若求排列数, 外层for循环遍历背包, 内层遍历物品
    for i in range(len(coins)):
        for j in range(coins[i], amount+1):
            dp[j] += dp[j - coins[i]]  # 递推公式
    return dp[amount]


if __name__ == "__main__":
    print aa(5, [1, 2, 5])
