# -*- coding: utf-8 -*-

# 题目: 给定一个无序的正整数数组, 找出数组中每个元素右边第一个比它大的数（若没有，则返回-1）

# 初始化res数组, 内容都为-1
# 初始化stack, 放入索引0, nums遍历时从1开始
# 遍历逻辑: 
#  当前元素大于栈顶元素, res[stack.pop()] = nums[i], 一直循环下去, 直到条件不满足为止
#  当前元素小于栈顶元素, 直接将当前元素索引放入栈中          
def aa(nums):
    if not nums: return []
    res, stack = [-1] * len(nums), [0]
    for i in range(1, len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res

if __name__ == "__main__":
    print aa([8,2,5,4,3,9,7,2,5])
