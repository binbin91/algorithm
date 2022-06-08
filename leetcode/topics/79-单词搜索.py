# -*- coding: utf-8 -*-


# 判断单词是否存在与二维数组中的依据是
# 1. 单词存在与二维数组必须是按照字母顺序, 且构建单词字母必须是相邻单元格
# 2. 同个单元格字母不能重复使用
#
# 解题
# 1. 默认从坐标(0,0)开始搜索, 先找到单词首字母, 然后对其进行标记(防止重复使用)
# 2. 然后向四个方向进行扩散搜索，对单元格的字母与单词中的字母进行比对
#    a) 若匹配, 则进行标记, 继续扩散搜索
#    b) 若不匹配, 尝试其他方向
#    c) 若完全不匹配(4个方向都不匹配), 则进行回退, 同时释放当前单元格的标记
# 重复上述步骤, 当单词完全匹配返回True, 否则返回False
def aa(board, word):
    m, n = len(board), len(board[0])
    dp = [[False] * n for _ in range(m)]
    rows = [-1, 0, 1, 0]
    cols = [0, 1, 0, -1]
    
    def dfs(x, y, idx):
        if board[x][y] != word[idx]: return False
        if idx == len(word) - 1: return True

        dp[x][y] = True
        for i in range(4):
            nx, ny = x + rows[i], y + cols[i]
            if 0 <= nx < m and 0 <= ny < n and not dp[nx][ny] and dfs(nx, ny, idx+1): return True
 
        dp[x][y] = False
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0): return True
    return False


if __name__ == "__main__":
    print aa([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    print aa([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    print aa([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
