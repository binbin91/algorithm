# -*- coding: utf-8 -*-


def aa(nums):
    n = len(nums)
    points = [1] + nums + [1]
    dp = [[0] * (n+2) for _ in range(n+2)]

    for i in range(n, -1, -1):
        for j in range(i+1, n+2):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i] * points[j] * points[k]) 
    return dp[0][-1]


if __name__ == "__main__":
    print aa([3,1,5,8])
    print aa([1,5])
