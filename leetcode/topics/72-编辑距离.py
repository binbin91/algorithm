# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(w1, w2):
    # dp数组, 以下标i-1结尾的字符串w1, 和以下标j-1结尾的字符串w2, 最近编辑距离为dp[i][j]
    dp = [[0] * (len(w2)+1) for _ in range(len(w1)+1)] 
    for i in range(len(w1)+1):
        dp[i][0] = i
    for j in range(len(w2)+1):
        dp[0][j] = j
    # 递推公式
    # w1[i-1] == w2[j-1], 不用编辑即dp[i-1][j-1]
    # w1[i-1] != w2[j-1]
    #  删除操作
    #    w1删除一个元素, 就是以下标i-2结尾的w1与j-1为结尾的w2的最近编辑距离再加上一个操作，即dp[i-1][j] + 1
    #    w2删除一个元素, 就是以下标i-1结尾的w1与j-2为结尾的w2的最近编辑距离再加上一个操作，即dp[i][j-1] + 1
    #  添加操作等同删除操作，即w2添加一个元素, 相等于w1删除一个元素  
    #  替换操作
    #    w1替换w[i-1], 使其与w2[j-1]相同, 此时不增加元素
    #    那么下标i-2为结尾的w1与j-2结尾的w2的最近编辑距离加上一个替换操作，即dp[i-1][j-1] + 1 
    # 综上, 当w[i-1] != w[j-1]时取最小的, 即min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    for i in range(1, len(w1)+1):
        for j in range(1, len(w2)+1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # 递推公式
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    return dp[-1][-1]


if __name__ == "__main__":
    print aa("horse", "ros")
