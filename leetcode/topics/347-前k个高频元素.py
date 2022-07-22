# -*- coding: utf-8 -*-

import heapq


def aa(nums, k):
    # 统计元素出现频率
    mp = {} 
    for i in range(len(nums)):
        mp[nums[i]] = mp.get(nums[i], 0) + 1

    # 定一个小顶堆, 对频率进行排序
    pri_que = []
    for key, freq in mp.items():
        heapq.heappush(pri_que, (freq, key))
        # 若堆大小大于k, 则进行队列弹出
        if len(pri_que) > k: 
            heapq.heappop(pri_que)

    # 找出前k个高频元素(小顶堆先弹出最小的元素, 所以倒序进行数组输出)
    res = [0] * k
    for i in range(k-1, -1, -1):
        res[i] = heapq.heappop(pri_que)[1]
    return res

if __name__ == "__main__":
    print aa([1,1,1,2,2,3], 2)
