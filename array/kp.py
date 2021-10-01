# -*- coding: utf-8 -*-

def aa(data, l, h):
    i = l - 1
    p = data[h] 
    print '基准:', p
    for j in range(l, h):
        if data[j] <= p:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[h] = data[h], data[i+1]
    return i+1

def quick(data, l, h):
    print l, h, data
    if l<h:
        p = aa(data, l, h)
        quick(data, l, p-1)
        quick(data, p+1, h)

if __name__ == "__main__":
    data = [10,7,8,9,1,5]
    quick(data, 0, len(data)-1)
    print data
