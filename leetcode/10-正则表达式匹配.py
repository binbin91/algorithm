# -*- coding: utf-8 -*-

# 解体思路: 从s[:1]和p[:1]是否能匹配开始判断，每轮添加一个字符判断是否匹配, 直至添加完整个字符串s和p
# dp动态规划:
#   状态定义: 设定dp动态规划矩阵，dp[i][j]代表字符串s的前i个字符和p的前j个字符能够匹配
#   转换方程: dp[0][0]是空字符状态, 因此dp[i][j]对应添加的字符是s[i-1]和p[j-1]
#      当p[j-1] = '*'时, 以下任意一种情况为true时等于true
#         1. dp[i][j-2]: p[j-2]* 看作出现0次，能否匹配
#         2. dp[i-1][j] 且 s[i-1] = p[j-2]: p[j-2]多出现一次时，能否匹配
#         3. dp[i-1][j] 且 p[j-2] = '.': '.'字符多出现一次时，能否匹配
#      当p[j-1] != '*', 以下任意一种情况为true时等于true
#         1. dp[i-1][j-1] 且 s[i-1] = p[j-1]: p[i-1]多出现一次时，能否匹配
#         2. dp[i-1][j-1] 且 p[j-1] = '.': s[i-1]时, 能否匹配
#
# 初始化: 
#   dp[0][0] = true, 代表两个空字符串能否匹配
#   dp[0][j] = dp[0][j-2]且p[j-1] = '*':  首行s为空字符串, 因此p的偶数位为*时才能够匹配，因此遍历字符串p, 步长为2(只看偶数位)
# 返回值: dp矩阵右下角字符, 代表字符串s和p能否匹配

def aa(s, p):
    m, n = len(s)+1, len(p)+1

    # 矩阵初始化
    dp = [[False] * n for _ in range(m)]
    dp[0][0] = True
    for j in range(2, n, 2):
        dp[0][j] = dp[0][j-2] and p[j-1] == '*'

    for i in range(1, m):
        for j in range(1, n):
            if p[j-1] == '*':
                if dp[i][j-2]: 
                    dp[i][j] = True
                elif dp[i-1][j] and s[i-1] == p[j-2]:
                    dp[i][j] = True
                elif dp[i-1][j] and p[j-2] == '.':
                    dp[i][j] = True
            else:
                if dp[i-1][j-1] and s[i-1] == p[j-1]:
                    dp[i][j] = True
                elif dp[i-1][j-1] and p[j-1] == '.':
                    dp[i][j] = True

    return dp[-1][-1]

if __name__ == "__main__":
    s = "aa"
    p = "a*"
    print aa(s,p)
