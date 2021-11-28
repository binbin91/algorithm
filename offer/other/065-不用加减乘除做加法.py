# -*- coding: utf-8 -*-

def aa(a,b):
    x = 0xffffffff
    a, b = a&x, b&x
    while b != 0:
        a,b = (a^b), (a&b) << 1 & x
    return a if a <= 0x7fffffff else ~(a^x)


if __name__ == "__main__":
    a, b = 1,1
    print aa(a,b)
