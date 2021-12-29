# -*- coding: utf-8 -*-


def aa(n):
    dp = [0] * (len(n))
    dp[0] = n[0]
    dp[1] = n[1]
    for i in range(2, len(n)):
        dp[i] = min(dp[i-1], dp[i-2]) + n[i]
    return min(dp[len(n)-1], dp[len(n)-2])


if __name__ == "__main__":
    print aa([10,15,20])
