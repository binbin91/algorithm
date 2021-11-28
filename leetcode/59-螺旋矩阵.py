# -*- coding: utf-8 -*-

def aa(n):
    m = [[0] * n for _ in range(n)]
    l, r, u, d = 0, n-1, 0, n-1
    number = 1
    while l < r and u < d:
        # 从左到右填充上边
        for i in range(l, r):
            m[u][i] = number
            number += 1
        # 从上到下填充右边
        for i in range(u, d):
            m[i][r] = number
            number += 1
        # 从右到左填充下边
        for i in range(r, l, -1):
            m[d][i] = number
            number += 1
        # 从下到上填充左边
        for i in range(d, u, -1):
            m[i][l] = number
            number += 1
        l += 1
        r -= 1
        u += 1
        d -= 1
    
    if n % 2:
        m[n//2][n//2] = number    
    return m 


if __name__ == "__main__":
    print aa(3)
