# -*- coding: utf-8 -*-


# 已知整数数组且非空, 只有某个元素出现一次，其余出现两次
# 想到位运算的异或, 两个相同的数字异或的结果为0
# 即遍历整个数组，让数组所有元素异或, 得到的结果就是只出现一次的那个元素
def aa(nums):
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
    return nums[0]


if __name__ == "__main__":
    print aa([2,2,1])
    print aa([4,1,2,1,2])
