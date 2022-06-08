# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n+1):
        for j in range(1,3):
            if i >= j:
                dp[i] += dp[i-j]
    return dp[-1]


if __name__ == "__main__":
    print aa(5)
