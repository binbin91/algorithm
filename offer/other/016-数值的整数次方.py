# -*- coding: utf-8 -*-

def aa(x, n):
    if x == 0: return 0
    res = 1
    if n < 0: x, n = 1/x, -n
    while n:
        if n & 1: res *= x
        x *= x
        n >>= 1
    return res


if __name__ == "__main__":
    x = 2.00000
    n = 10
    print aa(x, n)
