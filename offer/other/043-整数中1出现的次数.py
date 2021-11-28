# -*- coding: utf-8 -*-

def aa(n):
    digit, res = 1,0
    high, cur, low = n//10, n%10, 0
    while high != 0 or cur != 0:
        if cur == 0: res += high * digit
        elif cur == 1: res += high * digit + low + 1
        else: res += (high+1) * digit
        low += cur * digit
        cur = high % 10
        high //= 10
        digit *= 10
    return res



if __name__ == "__main__":
    print aa(12)
    print aa(13)
