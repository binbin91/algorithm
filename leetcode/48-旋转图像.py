# -*- coding: utf-8 -*-

# 原地修改, O(1)复杂度
# 设矩阵左上角元素A, 右上角元素B, 右下角元素C, 左下角元素D, 90度旋转矩阵
# 等同于依次执行D->A, C-D, B-C, A-B
# 借助辅助变量存元素A, 避免D->A，丢失了A
def aa(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range((n+1)//2):
            tmp = matrix[i][j]
            matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] = matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], tmp
    return matrix

if __name__ == "__main__":
    print aa([[5,1,9,11], [2,4,8,10], [13,3,6,7], [15,14,12,16]])
    print aa([[1,2,3], [4,5,6], [7,8,9]])
