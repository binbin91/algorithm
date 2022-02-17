# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1,n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[m-1][n-1]


if __name__ == "__main__":
    print aa(3,7)
