# -*- coding: utf-8 -*-

# 使用字典存储每个端点值对应的区间长度
# 若值已在字典里, 则跳过
# 若值不在, 取出其左右相邻已有连续区间长度left和right，计算区间长度(l+r+1), 更新最大长度(res)和区间两端点的长度值
def aa(nums):
    mp, max_lg = dict(), 0
    for i in nums: 
        if i not in mp:
            l, r = mp.get(i-1, 0), mp.get(i+1, 0)
            cur_lg = 1 + l + r
            if cur_lg > max_lg: max_lg = cur_lg
            mp[i] = mp[i-l] = mp[i+r] = cur_lg
    return max_lg 


if __name__ == "__main__":
    print aa([100,4,200,1,3,2])
    print aa([0,3,7,2,5,8,4,6,0,1])
