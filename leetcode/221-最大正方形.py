# -*- coding: utf-8 -*-


def aa(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    mx = 0

    for i in range(m):
        if matrix[i][0] == '1': dp[i][0], mx = 1, 1

    for i in range(1, n):
        if matrix[0][i] == '1': dp[0][i], mx = 1, 1
 
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                mx = max(mx, dp[i][j])
    return mx * mx


if __name__ == "__main__":
    print aa([["0"]])
    print aa([["0", "1"], ["1", "0"]])
