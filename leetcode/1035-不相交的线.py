# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(A, B):
    dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
    # 递推公式
    # A[i-1]与B[j-1]相等, 那么找到相同公共元素, dp[i][j] = dp[i-1][j-1] + 1
    # A[i-1]与B[j-1]不相等，那么从A[0,i-2]与B[0,j-1]的最长公共子序列和A[0,i-1]与B[0,j-2]的最长公共子序列取最大的, 即max(dp[i-1][j], dp[i][j-1])
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1  # 递推公式
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1] 


if __name__ == "__main__":
    print aa([1,4,2], [1,2,4])
    print aa([2,5,1,2,5], [10,5,2,1,5,2])
