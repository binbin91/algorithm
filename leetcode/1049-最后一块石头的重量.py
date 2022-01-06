# -*- coding: utf-8 -*-

def aa(stones):
    sw = sum(stones)
    target = sw // 2
    dp = [0] * 15001
    for i in range(len(stones)):
        for j in range(target, stones[i]-1, -1):  # dp[j - stones[i]]为 容量为j - stones[i]的背包最大所背重量
            dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])  # 递推公式
    return sw - 2 * dp[target]


if __name__ == "__main__":
    print aa([2,7,4,1,8,1])
