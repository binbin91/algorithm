# -*- coding: utf-8 -*-

def aa(n):
    res = 0
    while n:
        res += 1
        n &= n-1
    return res


if __name__ == "__main__":
    print aa(11)
    print aa(128)
    print aa(4294967293)
