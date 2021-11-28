# -*- coding: utf-8 -*-

import collections

# 解题思路 
#   zip(range(), range())实现滑动窗口左右边界, 同时遍历
#   辅助队列存储已形成窗口的元素, 将队首元素出栈存入列表
def aa(nums, k):
    queue = collections.deque()
    res, n = [], len(nums)
    for i,j in zip(range(1-k, n+1-k), range(n)):
        if i > 0 and queue[0] == nums[i-1]:
            queue.popleft()
        while queue and queue[-1] < nums[j]:
            queue.pop()
        queue.append(nums[j])
        if i >= 0: res.append(queue[0])
    return res

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print aa(nums, k)
