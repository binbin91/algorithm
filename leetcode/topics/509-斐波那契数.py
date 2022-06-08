# -*- coding: utf-8 -*-


def aa(n):
    if n < 2: return
    a, b, c = 0, 1, 0
    for _ in range(1, n):
        c = a + b
        a, b = b, c
    return c


if __name__ == "__main__":
    print aa(10)
