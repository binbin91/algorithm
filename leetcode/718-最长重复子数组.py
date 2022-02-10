# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 连续子序列
def aa(A, B):
    # dp数组, 以下标i-1为结尾的A和以下标j-1为结尾的B, 最长重复子数组长度为dp[i][j]
    dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
    res = 0
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1  # 递推公式
            res = max(res, dp[i][j])
    return res


if __name__ == "__main__":
    print aa([1,2,3,2,1], [3,2,1,4,7])
