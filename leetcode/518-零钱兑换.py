# -*- coding: utf-8 -*-

def aa(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], amount+1):
            dp[j] += dp[j - coins[i]]  # 递推公式
    return dp[amount]


if __name__ == "__main__":
    print aa(5, [1, 2, 5])
