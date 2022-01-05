# -*- coding: utf-8 -*-


def aa(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    curr = [0] * n
    for j in range(n):
        if obstacleGrid[0][j] == 1: break
        curr[j] = 1

    for i in range(1, m):
        for j in range(n):
            if obstacleGrid[i][j] == 1: curr[j] = 0
            elif j > 0: curr[j] = curr[j] + curr[j-1]
    return curr[n-1]


if __name__ == "__main__":
    print aa([[0,0,0],[0,1,0],[0,0,0]])
