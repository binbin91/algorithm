# -*- coding: utf-8 -*-


# 二维数组
def aa(bag_size, weight, v):
    rows, cols = len(weight), bag_size + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = 0

    fw, fv = weight[0], v[0]
    for j in range(1, cols):
        if fw <= j: dp[0][j] = fv

    # 更新dp数组, 先遍历物品再遍历背包
    for i in range(1, len(weight)):
        cw, cv = weight[i], v[i]
        for j in range(1, cols):
            if cw > j: dp[i][j] = dp[i-1][j] # 说明背包装不下物品, 所以不装
            else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-cw] + cv)  # 定义dp数组, dp[i][j] 前i个物品里, 放进容量为j的背包, 价值总和最大是多少
    return dp


# 一维数组
def bb(bag_size, weight, value):
    dp = [0] * (bag_size + 1)
    # 先遍历物品, 再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_size, weight[i]-1, -1):
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])  # 递推公式
    return dp
