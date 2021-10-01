# -*- coding: utf-8 -*-

def aa(data, k):
    if not data: return 0
    first = firstk(data, k)
    last = lastk(data, k)
    if first == -1 or last == -1: return 0
    return last - first + 1

def firstk(data, k):
    low, high = 0, len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] < k:
            low = mid + 1
        elif data[mid] > k:
            high = mid - 1
        else:
            if mid == low or data[mid-1] != k:
                return mid
            else:
                high = mid - 1
    return -1

def lastk(data, k):
    low, high = 0, len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] > k:
            high = mid - 1
        elif data[mid] < k:
            low = mid + 1
        else:
            if mid == high or data[mid+1] != k:
                return mid
            else:
                low = mid + 1
    return -1

if __name__ == "__main__":
    array = [1,2,3,3,3,3,4,5]
    k = 3 
    #print aa(array, k)
    #print aa([1,3,3,3,3,4], k)
    print aa([1,3,3,3,3,4], 2)
