# -*- coding: utf-8 -*-

import collections

def aa(data):
    dic = collections.Counter(data)
    for k,v in dic.iteritems():
        if v > 1:
            return k
    return -1 

def bb(data):
    data.sort()
    pre = data[0]
    for i in range(1, len(data)-1):
        if pre == data[i]:
            return pre
        pre = data[i]
    return -1

def cc(data):
    i = 0
    while i < len(data):
        if data[i] == i:
            i += 1
            continue
        if data[data[i]] == data[i]:
            return data[i]
        data[data[i]], data[i] = data[i], data[data[i]]
    return -1


if __name__ == "__main__":
    data = [2,3,1,0,2,5,3]
    print aa(data)
    print bb([2,3,1,0,2,5,3])
    #print bb([2,3,1,0,5])
    print cc([2,3,1,0,2,5,3])
