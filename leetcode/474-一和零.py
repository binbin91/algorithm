# -*- coding: utf-8 -*-

def aa(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        o, z = s.count('1'), s.count('0') 
        for i in range(m, z-1, -1):
            for j in range(n, o-1, -1):
                dp[i][j] = max(dp[i][j], dp[i-z][j-o] + 1)  # 递推公式
    return dp[m][n]


if __name__ == "__main__":
    print aa( ["10", "0001", "111001", "1", "0"], 5, 3)
