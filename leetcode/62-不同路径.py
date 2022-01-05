# -*- coding: utf-8 -*-


def aa(m, n):
    dp = [[1 for i in range(n)] for j in range(m)]
    for i in range(1, m):
        for j in range(1,n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[m-1][n-1]


if __name__ == "__main__":
    print aa(3,7)
