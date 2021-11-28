# -*- coding: utf-8 -*-

def aa(array, k):
    if k >= len(array): return array
    def quick_sort(l,r):
        i,j = l,r
        while i<j:
            while i<j and array[j] >= array[l]: j-=1
            while i<j and array[i] <= array[l]: i+=1
            array[i], array[j] = array[j], array[i]
        array[l], array[i] = array[i], array[l]
        if k<i: return quick_sort(l, i-1)
        if k>i: return quick_sort(i+1, r)
        return array[:k]
    return quick_sort(0, len(array)-1)


if __name__ == "__main__":
    print aa([3,2,1], 2)
    print aa([0,1,2,1], 1)
