# -*- coding: utf-8 -*-

# 采用自定排序功能的数据结构-堆
# 堆中保留数据流中的前K大元素: 采用小根堆能保证每次调用堆的pop函数时, 从堆中删除的是堆中最小元素(堆顶)
# 小根堆中保留的一直是堆中的前K大的元素, 堆的大小是K, 所以堆顶元素是第K大元素

import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.que = nums
        heapq.heapify(self.que)

    def add(self, val):
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0] 


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    print obj.add(3)
    print obj.add(5)
    print obj.add(10)
    print obj.add(9)
    print obj.add(4)
