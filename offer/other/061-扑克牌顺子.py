# -*- coding: utf-8 -*-

def aa(nums):
    joker = 0
    # 数组排序
    nums.sort()
    for i in range(4):
        # 统计大小王数量
        if nums[i] == 0: joker += 1
        # 若有重复，提前返回false
        elif nums[i] == nums[i+1]: return False
    # 最大牌-最小牌 < 5, 则可构成顺子
    return nums[4] - nums[joker] < 5

if __name__ == "__main__":
    data = [1,2,3,4,5]
    print aa(data)
