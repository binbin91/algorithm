# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(t1, t2):
    l1, l2 = len(t1)+1, len(t2)+1
    # dp数组, 长度为[0, i-1]的字符串text1与长度[0,j-1]的字符串text2, 最长公共子序列为dp[i][j]
    dp = [[0 for _ in range(l1)] for _ in range(l2)] 
    for i in range(1, l2):
        for j in range(1, l1):
            if t1[j-1] == t2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1  # 递推公式
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1] 


if __name__ == "__main__":
    print aa("abcde", "ace")
