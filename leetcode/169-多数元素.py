# -*- coding: utf-8 -*-

# 摩尔投票法
# 遍历nums, 将当前票数最多候选人与其获得的票数(抵消后)分别存储在m与count中
# 每次遍历时，判断当前m是否为零, 为零直接将当前候选人赋值给m, 且count + 1
# 若m不等于零, 代表当前m的票数未被完全抵消, count - 1
def aa(nums):
    m, count = 0, 0
    for n in nums: 
        if count == 0: m = n
        if n == m: count += 1
        else: count -= 1
    return m


if __name__ == "__main__":
    print aa([3,2,3])
    print aa([2,2,1,1,1,2,2])
