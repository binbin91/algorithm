# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# PS, 回文子串是连续的，回文子序列可不是连续的
def aa(s):
    # dp数组, 字符串s在[i,j]范围内最长的回文子序列的长度为dp[i][j]
    dp = [[0] * len(s) for _ in range(len(s))] 
    for i in range(len(s)):
        dp[i][i] = 1
    # 递推公式
    # 相等, 即dp[i+1][j-1] + 2
    # 不相等, 说明s[i]和s[j]同时加入并不能增加[i,j]区间回文子串的长度, 那么看s[i] s[j]哪一个可以组成最长的回文子序列
    #    加入s[i]，即dp[i+1][j]
    #    加入s[j], 即dp[i][j-1]
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][-1] 


if __name__ == "__main__":
    print aa("bbbab")
