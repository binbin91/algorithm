# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(s, t):
    # dp数组, 以i-1结尾的s子序列中出现以j-1结尾的t的个数为dp[i][j]
    dp = [[0] * (len(t)+1) for _ in range(len(s)+1)] 
    # dp[i][0]表示以i-1结尾的s可以随便删除元素, 出现空字符的个数
    # 那么dp[i][0]一定为1，也就是把i-1结尾的s，删除所有元素, 出现空字符串的个数就是1
    for i in range(len(s)):
        dp[i][0] = 1
    # dp[0][j]一定为0, s无论如何改变也变成不了t
    for j in range(1, len(t)):
        dp[0][j] = 0
    # 递推公式
    # s[i-1]与t[j-1]相等, dp[i][j]可以有两部分组成
    #     一部分用s[i-1]来匹配, 那么个数为dp[i-1][j-1]
    #     一部分不用s[i-1]来匹配, 个数为dp[i-1][j]
    # 所以相等时, dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # s[i-1]与t[j-1]不相等, dp[i][j]只有一部分组成, 不用s[i-1]来匹配, 即dp[i-1][j]
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]  # 递推公式
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]


if __name__ == "__main__":
    print aa("rabbbit", "rabbit")
