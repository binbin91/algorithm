# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(s):
    # dp数组, 区间范围[i,j]的子串是否是回文子串, 如果是dp[i][j]为true，否则为false
    dp = [[False] * len(s) for _ in range(len(s))] 
    res = 0
    # 递推公式
    # 不相等, 即dp[i][j] = false
    # 相等
    #  1. 下标i与j相同, 同一个字符就是回文子串
    #  2. 下标i与j相差1, 也是回文子串
    #  3. 下标i与j相差大于1, 那么看区间i+1与j-1之间，是不是回文子串
    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                if j - i <= 1: res, dp[i][j] = res + 1, True   # 情况1与2
                elif dp[i+1][j-1]: res, dp[i][j] = res + 1, True  #情况3
    return res


if __name__ == "__main__":
    print aa("abc")
