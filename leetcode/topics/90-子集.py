# -*- coding: utf-8 -*-

# Carl哥, 回溯三部曲
# 1. 递归函数参数
# 2. 递归终止条件
# 3. 单层搜索逻辑
#
# 组合问题、子集问题和分割问题都抽象为一棵树, 组合与分割都是收集树的叶子节点, 而子集是找树的所有节点
# 求子集:
#   子集是无序的，[1,2]和[2,1]是一样的
#   既然无序, 取过的元素不会重复取, 遍历就需要从startIndex开始, 而不是从0开始
#   不需要任何剪枝, 因为子集就是要遍历整棵树

# 和78子集区别, 在于集合有重复元素, 求取的子集要去重
# 先对数组进行排序
# 去重逻辑: if i > startIndex and nums[i] == nums[i-1]: continue

def aa(nums):
    res, path = [], [] 
    def bak(nums, startIndex):
        res.append(path[:])
        if startIndex == len(nums):
            return
        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            bak(nums, i + 1)  # 递归
            path.pop() # 回溯
    nums = sorted(nums)
    bak(nums, 0)
    return res


if __name__ == "__main__":
    print aa([1,2,2])
