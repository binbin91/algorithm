# -*- coding: utf-8 -*-

def reOrderArray(array):
    odd_cnt = 0
    res = [0] * len(array)
    for i in array:
        if i % 2 != 0:
           odd_cnt += 1

    odd_i = 0
    even_i = odd_cnt
    for i in range(len(array)):
        if array[i] % 2 != 0:
            res[odd_i] = array[i]
            odd_i += 1
        else:
            res[even_i] = array[i]
            even_i += 1
    return res

if __name__ == "__main__":
    array = [1,2,3,4]
    print reOrderArray(array)
