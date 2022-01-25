# -*- coding: utf-8 -*-


def aa(n):
    if n < 0: return []
    res = []
    def dfs(p, l, r):
        if l > n or r > l: return
        if len(p) == n * 2:
	    res.append(p)
            return
        dfs(p + '(', l + 1, r)
        dfs(p + ')', l, r + 1)
    dfs('', 0, 0)
    return res


if __name__ == "__main__":
    print aa(2)
