# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            # 当左边和上边都为矩阵边界, 即起点则跳过
            if i == j == 0: continue
            # 当左边为矩阵边界
            elif i == 0: grid[i][j] = grid[i][j-1] + grid[i][j]
            # 当上边为矩阵边界
            elif j == 0: grid[i][j] = grid[i-1][j] + grid[i][j]
            # 当左边与上边都不是矩阵边界
            else: grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
    return grid[-1][-1]


if __name__ == "__main__":
    print aa([[1,3,1], [1,5,1], [4,2,1]])
    print aa([[1,2,3], [4,5,6]])
