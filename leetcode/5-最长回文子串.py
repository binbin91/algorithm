# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(s):
    n = len(s)
    if n < 2: return s
    max_len, res = 1, s[0]
    dp = [[[False] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for j in range(1, n):
        for i in range(0, i):
            if s[i] != s[j]:
                dp[i][j] = False 
            else:
                if j -i <= 2: dp[i][j] = True
                else: dp[i][j] = dp[i+1][j-1]
                if dp[i][j] == True and j - i+1 > max_len:
                    max_len = j - i + 1
                    res = s[i:j+1]
    return res


if __name__ == "__main__":
    print aa("babad")
