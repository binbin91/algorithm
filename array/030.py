# -*- coding: utf-8 -*-

def aa(array):
    for i in range(1, len(array)):
        array[i] += max(array[i-1], 0)
    return max(array)


if __name__ == "__main__":
    array = [6,-3,-2,7,-15,1,2,2] 
    print aa(array)
