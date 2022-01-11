# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 背包递推公式
# 问能否装满背包 or 最多装多少: dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
# 问装满背包有几种方法: dp[j] += dp[j-nums[i]]
# 问背包装满最大价值: dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
# 问装满背包所有物品的最小个数: dp[j] = min(dp[j], dp[j-coins[i]] + 1)

# 遍历顺序
# 01背包: 
#   二维dp数组两种遍历方式都可以, 但内层for循环是从小到大
#   一维dp数组只能先遍历物品再遍历背包, 内层for循环是从大到小
# 完全背包:
#   求组合数, 先遍历物品再遍历背包
#   求排列数, 先遍历背包再遍历物品
#   求最小数, 都可以

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
