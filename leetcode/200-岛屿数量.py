# -*- coding: utf-8 -*-


# 从岛屿某一点(i, j)，从上下左右做深度搜索, 若(i,j)越过边界 or grid[i][j] == 0越过边界, 即终止
# 遍历整个矩阵，若grid[i][j] == 1时，进行深度优先搜索且岛屿数加1, 最终返回岛屿数 
def aa(grid):
    def dfs(grid, i, j):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return
        grid[i][j] = '0'   # 避免重复搜索
        dfs(grid, i + 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i - 1, j)
        dfs(grid, i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

if __name__ == "__main__":
    print aa([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ])
    print aa([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ])
