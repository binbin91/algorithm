# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(n):
    dp = [0] * (len(n))
    dp[0] = n[0]
    dp[1] = n[1]
    for i in range(2, len(n)):
        dp[i] = min(dp[i-1], dp[i-2]) + n[i]
    return min(dp[len(n)-1], dp[len(n)-2])


if __name__ == "__main__":
    print aa([10,15,20])
