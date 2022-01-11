# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(n):
    # dp数组, 和为i的完全平方数的最少数量为dp[j]
    dp = [n] * (n + 1) 
    dp[0] = 0 # 仅为了推导递推公式
    # 先遍历背包, 再遍历物品, 本题两种遍历方式都可以
    for j in range(1, n + 1):
        for i in range(1, n):
            num = i ** 2
            if num > j: break
            if j - num >= 0: dp[j] = min(dp[j], dp[j-num] + 1)  # 递推公式
    return dp[n]


if __name__ == "__main__":
    print aa(12)
