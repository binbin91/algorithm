# -*- coding: utf-8 -*-


def aa(n, k):
    res, path = [], []
    def recur(n, k, s):
        if len(path) == k: 
            res.append(path[:])
            return
        for i in range(s, n-(k-len(path))+2):
            path.append(i)
            recur(n, k, i+1)
            path.pop()
    recur(n, k, 1)
    return res 
