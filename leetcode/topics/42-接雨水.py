# -*- coding: utf-8 -*-

# 双指针
def aa(height):
    res = 0
    for i in range(len(height)):
        # 第一个柱子和最后一个柱子不接雨水
        if i == 0 or i == len(height)-1: continue
        # 记录左右柱子的最高高度
        l, r = height[i-1], height[i+1]
        for j in range(i-1):
            if height[j] > l: l = height[j]
        for k in range(i+2, len(height)):
            if height[k] > r: r = height[k]
        # 左右柱子高度最小值, 减去雨水高度, 就是列的雨水体积
        res1 = max(min(l, r) - height[i], 0)
        # 每列雨水体积相加就是总雨水体积
        res += res1 
    return res 

# DP
def bb(height):
    n = len(height)
    l, r = [0] * n, [0] * n 

    # 计算左柱子高度
    l[0] = height[0]
    for i in range(1, n):
        l[i] = max(l[i-1], height[i])

    # 计算右柱子高度
    r[-1] = height[-1]
    for i in range(n-2, -1, -1):
        r[i] = max(r[i+1], height[i])
   
    res = 0
    for i in range(0, n):
        # 当前列雨水面积
        s = min(l[i], r[i]) - height[i]
        res += s
    return res 


if __name__ == "__main__":
    print bb([0,1,0,2,1,0,1,3,2,1,2,1])
    print bb([4,2,0,3,2,5])
