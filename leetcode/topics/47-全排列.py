# -*- coding: utf-8 -*-

# Carl哥, 回溯三部曲
# 1. 递归函数参数
# 2. 递归终止条件
# 3. 单层搜索逻辑
#
# 求排列:
#   排列是有序的, [1,2]和[2,1]是两个集合
#   当收集元素数组path大小和nums数组一样大的时候，说明找到一个全排列, 也表示到达叶子节点
#   排列问题, 每次都从头开始搜索, 例如元素1在[1,2]中已使用过, 但是在[2,1]中还要再使用一次

# 和46区别在于, 给定一个可包含重复数字的序列, 要返回所有不重复的排列
# 排列去重套路, 和子集、组合去重套路是一样的, 先排序再去重

def aa(nums):
    # res存放符合条件结果的集合, path用来存放符合条件的结果, used用来树枝去重
    res, path, used = [], [], [0] * len(nums)
    def bak(nums, used):
        if len(path) == len(nums):
            return res.append(path[:]) # 已找一个全排列

        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue 
                used[i] = 1
                path.append(nums[i])
                bak(nums, used)  # 递归
                path.pop() # 回溯
                used[i] = 0
    nums = sorted(nums)
    bak(nums, used)
    return res


if __name__ == "__main__":
    print aa([1,1,2])
    print aa([1,2,3])
