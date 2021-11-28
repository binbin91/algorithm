# -*- coding: utf-8 -*-

def aa(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a % 1000000007


if __name__ == "__main__":
    print aa(2)
    print aa(5)
