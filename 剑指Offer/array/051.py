# -*- coding: utf-8 -*-

# 计算下三角乘积, 再计算上三角乘积

def aa(data):
    if len(data) < 1:
        return data

    b, tmp = [1] * len(data), 1
    for i in range(1, len(data)):
        b[i] = b[i-1] * data[i-1]
    
    for i in range(len(data)-2, -1, -1):
        tmp *= data[i+1]
        b[i] *= tmp
    return b

if __name__ == "__main__":
    data = [1,2,3,4,5]
    print aa(data)
    print aa([1,2])
    print aa([1])
