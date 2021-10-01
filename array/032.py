# -*- coding: utf-8 -*-

import functools

def sort_rule(x,y):
    a,b = x+y, y+x
    if a>b: return 1
    elif a<b: return -1
    else: return 0


def print_min_numer(array):
    strs = [str(i) for i in array]
    strs.sort(key=functools.cmp_to_key(sort_rule))
    return ''.join(strs)


def aa(data):
    def fast_sort(l, r):
        if l >= r: return 
        i, j = l, r
        while i < j:
            while strs[j] + strs[i] >= strs[l] + strs[j] and i < j: j -= 1
            while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
            strs[i], strs[j] = strs[j], strs[i]
        strs[i], strs[l] = strs[l], strs[i]
        fast_sort(l, i-1)
        fast_sort(i+1, r)
        
    strs = [str(num) for num in data]
    fast_sort(0, len(strs) - 1)
    return ''.join(strs)


if __name__ == "__main__":
    array = [3,32,321] 
    print print_min_numer(array)
    print aa([3,32,321])
