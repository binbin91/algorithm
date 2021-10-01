# -*- coding: utf-8 -*-

def aa(data, k):
    if not data:
        return 0
    i = 0
    j = len(data) - 1
    while i<j and data[i] != data[j]:
        if data[i] < k:
            i += 1
        if data[j] > k:
            j -= 1
    if data[i] != k:
        return 0
    return j-i+1

if __name__ == "__main__":
    array = [1,2,3,3,3,3,4,5]
    k = 3 
    print aa(array, k)
