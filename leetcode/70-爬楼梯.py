# -*- coding: utf-8 -*-


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
