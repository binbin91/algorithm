# -*- coding: utf-8 -*-

import collections

def aa(array):
    dic = collections.Counter(array)
    for k,v in dic.items():
        if v > len(array)/2:
            return k

if __name__ == "__main__":
    array = [1,2,3,2,2,2,5,4,2]
    print aa(array)
    print aa([1,2,3,4])
