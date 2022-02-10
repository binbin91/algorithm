# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(s, t):
    # dp数组, 以下标i-1结尾的字符串s, 和以下标j-1结尾的字符串t, 相同子序列的长度为dp[i][j]
    dp = [[0] * (len(t)+1) for _ in range(len(s)+1)] 
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1  # 递推公式
            else:
                dp[i][j] = dp[i][j-1]
    return True if dp[-1][-1] == len(s) else False


if __name__ == "__main__":
    print aa("abc", "ahbgdc")
