# -*- coding: utf-8 -*-

# 双指针解法
# 初始化pre指针和count(用于统计破坏性数字个数)
# pre赋值需要考虑nums[i]和nums[i-1]被删的情况
def aa(nums):
    pre, count = nums[0], 0
    for i in range(1, len(nums)):
        if nums[i] <= pre:
            count += 1
            if count > 1: 
                return False
            if nums[i] <= nums[i-2]:
                pre = nums[i-1]
            else:
                pre = nums[i]
        else:
            pre = nums[i]
    return count <= 1

# 栈
def bb(nums):
    stack, count = [], 0
    for i in nums:
        if not stack or i > stack[-1]:
            stack.append(i)
        else:
            count += 1
            if count > 1:
                return False
            temp = stack.pop()
            if not stack or i > stack[-1]:
                stack.append(i)
            else:
                stack.append(temp)
    return True


if __name__ == "__main__":
    print bb([1,2,10,5,7])
    print bb([2,3,1,2])
    print bb([1,1,1])
    print bb([1,2,3])
    print bb([4,4,3,3,4])
    print bb([1,2,7,4,5])
