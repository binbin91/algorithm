# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(w1, w2):
    # dp数组, 以i-1结尾的字符串w1, 和以j-1结尾的字符串w2, 若达到相等所需删除元素的最少次数dp[i][j]
    dp = [[0] * (len(w1)+1) for _ in range(len(w2)+1)] 
    for i in range(len(w1)+1):
        dp[i][0] = i
    for j in range(len(w2)+1):
        dp[0][j] = j
    for i in range(1, len(w1)+1):
        for j in range(1, len(w2)+1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # 递推公式
            else:
                dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j] + 1, dp[i][j-1] + 1)
    return dp[-1][-1]


if __name__ == "__main__":
    print aa("sea", "eat")
