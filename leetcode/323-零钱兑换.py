# -*- coding: utf-8 -*-

def aa(coins, amount):
    # dp数组, 凑成总金额j货币组合数为dp[j]
    dp = [amount + 1] * (amount + 1) 
    # dp数组初始化, 凑成总金额0的货币组合数为1
    dp[0] = 0
    # 先遍历物品(钱币),再遍历背包(总金额)
    # 本题求钱币最小个数(完全背包), 两种for循环都不会影响最终结果
    for i in coins:
        for j in range(i, amount+1):
            dp[j] = min(dp[j], dp[j-i] + 1)  # 递推公式
    return dp[amount] if dp[amount] < amount + 1 else -1


if __name__ == "__main__":
    print aa([1, 2, 5], 5)
