# -*- coding: utf-8 -*-

def aa(nums):
    if nums <= 3: return nums
    
    a,b,sums = 1,2,0
    for _ in range(3, nums+1):
        sums = a+b
        a = b
        b = sums
    return sums


if __name__ == "__main__":
    data = 5 
    print aa(5)
