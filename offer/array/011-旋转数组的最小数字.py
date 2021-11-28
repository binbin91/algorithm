# -*- coding: utf-8 -*-

def minArray(num):
    i, j = 0, len(num) - 1
    while i < j:
        m = (i + j) / 2
        if num[m] > num[j]: i = m + 1
        elif num[m] < num[j]: j = m
        else: j -= 1
    return num[i]

if __name__ == "__main__":
    num = [3,4,5,1,2]
    print minArray(num)
