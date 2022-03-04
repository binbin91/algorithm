# -*- coding: utf-8 -*-


def aa(nums, k):
    total, res, count = 0, 0, {}
    for n in nums: 
        total += n
        if total == k: res += 1
        if total - k in count: res += count[total-k]
        count[total] = count.get(total, 0) + 1 
    return res

if __name__ == "__main__":
    print aa([1,1,1], 2)
    print aa([1,2,3], 3)
