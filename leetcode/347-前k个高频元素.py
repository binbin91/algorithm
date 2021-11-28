# -*- coding: utf-8 -*-

import heapq


def aa(nums, k):
    mp = {} 
    for i in range(len(nums)):
        mp[nums[i]] = mp.get(nums[i], 0) + 1

    pri_que = []
    for key, freq in mp.items():
        heapq.heappush(pri_que, (freq, key))
        if len(pri_que) > k: 
            heapq.heappop(pri_que)

    res = [0] * k
    for i in range(k-1, -1, -1):
        res[i] = heapq.heappop(pri_que)[1]
    return res

if __name__ == "__main__":
    print aa([1,1,1,2,2,3], 2)
