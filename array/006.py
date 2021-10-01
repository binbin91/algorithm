# -*- coding: utf-8 -*-

def minArray(num):
    low, high = 0, len(num) - 1
    while low < high:
        mid = (high + low) / 2
        if num[mid] > num[high]:
            low = mid + 1
        elif num[mid] < num[high]:
            high = mid
        else:
            if num[high-1] > num[high]:
                low = high
                break
            high -= 1
    return num[low]

if __name__ == "__main__":
    num = [3,4,5,1,2]
    print minArray(num)
