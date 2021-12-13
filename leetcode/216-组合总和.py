# -*- coding: utf-8 -*-


def aa(k, n):
    res, path = [], []
    def recur(n, k, sum, s):
        if sum > n: return
        if sum == n and len(path) ==k: 
            res.append(path[:])
        for i in range(s, 9-(k-len(path))+2):
            path.append(i)
            sum += i
            recur(n, k, sum, i+1)
            sum -= i
            path.pop()
    recur(n, k, 0, 1)
    return res 
