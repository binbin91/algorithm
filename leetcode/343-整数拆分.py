# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(n):
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n+1):
        for j in range(1, n-1):
            dp[i] = max(dp[i], max(j * (i-j), j * dp[i-j]))
    return dp[n]


if __name__ == "__main__":
    print aa(2)
