# -*- coding: utf-8 -*-

# 解体思路:
#   采用滑动窗口解法(不断调节子序列起始位置和终止位置, 得出结果)
#   窗口是, 满足其和>=s的长度最小的连续子数组
#   起始位置移动，若当前窗口值大于s, 窗口就要向前移动
#   结束位置移动，遍历数组的指针(for循环里的索引)


def aa(s, nums):
    res, sum, index = float("inf"), 0, 0
    for i in range(len(nums)):
        sum += nums[i]
        # 若子序列和大于s, 调节起始位置
        while sum >= s:
            # 获取子序列长度
            res = min(res, i-index+1)
            # 调节起始位置
            sum -= nums[index]
            index += 1
    return 0 if res == float("inf") else res 


if __name__ == "__main__":
    print aa(7, [2,3,1,2,4,3])
