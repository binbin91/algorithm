# -*- coding: utf-8 -*-

import heapq


# 仅用做AC
def aa(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k: heapq.heappop(heap)
    return heap[0]


if __name__ == "__main__":
    print aa([3,2,1,5,6,4], 2)
    print aa([3,2,3,1,2,4,5,5,6], 4)
