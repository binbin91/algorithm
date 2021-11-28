# -*- coding: utf-8 -*-

from collections import deque


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


if __name__ == "__main__":
    print aa([1,3,-1,-3,5,3,6,7], 3)
