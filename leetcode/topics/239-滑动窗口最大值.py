# -*- coding: utf-8 -*-

from collections import deque

# 解体思路
#   利用双端队列记录当前窗口元素索引
#   若队列最左侧索引不在窗口范围内则弹出,
#   通过循环确保队列最左侧索引的数值最大
#   将最大值保存进res


def aa(nums, k):
    queue, res = deque(), []
    n = len(nums)
    for i,j in zip(range(1-k, n+1-k), range(n)):
        if i > 0 and queue[0] == nums[i-1]:
            queue.popleft()
        while queue and queue[-1] < nums[j]:
            queue.pop()
        queue.append(nums[j])
        if i >= 0: res.append(queue[0])
    return res


def bb(nums, k):
    queue, res = deque(), []
    for i, num in enumerate(nums):
        if queue and queue[0] == i - k:
            queue.popleft()
        while queue and nums[queue[-1]] < num:
            queue.pop()
        queue.append(i)
        if i >= k-1:
            res.append(nums[queue[0])
    return res


if __name__ == "__main__":
    print aa([1,3,-1,-3,5,3,6,7], 3)
