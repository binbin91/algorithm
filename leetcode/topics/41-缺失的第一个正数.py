# -*- coding: utf-8 -*-

# 要求常数级别的额外空间
# 方法一: 哈希表(空间复杂度不符合要求)
#   1. 数组元素放入哈希表
#   2. 使用O(1)时间复杂度判断某个正整数是否在这个数值中

# 方法二: 原地交换
#   此方法借鉴剑指Offer03 原地交换解题思路
#      1. 长度n的数组里里所有数字都在0~n-1范围内, 数组元素的的索引和值是一对多的关系
#      2. 因此可遍历数组通过交换操作，使元素的索引与值一一对应(即nums[i] = i), 通过索引映射的值起到字典作用
#    
#   1. 在一个长度为n的数组nums里, 我们要找的数就在[1,n+1]里, 若前面n个元素找不到情况下, 直接返回n+1
#   2. 数字1放入下标0位置, 数字2放入下标1位置, 按照这个思路原地交换一遍数组
#   3. 再遍历数组, 第一个遇到它的值不等于下标的那个数, 就是缺失的的第一个正数

def aa(nums):
    size = len(nums)
    for i in range(size):
        while 1 <= nums[i] <= size and nums[i] != nums[nums[i]-1]:
            swap(nums, i, nums[i]-1)
    for i in range(size):
        if i + 1 != nums[i]: return i + 1
    return size + 1

def swap(nums, i1, i2):
    nums[i1], nums[i2] = nums[i2], nums[i1]


if __name__ == "__main__":
    print aa([1,2,0])
    print aa([3,4,-1,1])
    print aa([7,8,9,11,12])
