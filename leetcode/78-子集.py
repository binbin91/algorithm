# -*- coding: utf-8 -*-

# Carl哥, 回溯三部曲
# 1. 递归函数参数
# 2. 递归终止条件
# 3. 单层搜索逻辑

# 组合问题、子集问题和分割问题都抽象为一棵树, 组合与分割都是收集树的叶子节点, 而子集恶事找树的所有节点

# 1. 子集是无序的，[1,2]和[2,1]是一样的
# 2. 既然无序, 取过的元素不会重复取, 遍历就需要从startIndex开始, 而不是从0开始

def aa(nums):
    # res存放符合条件结果的集合, path用来存放符合条件的结果
    res, path = [], [] 
    def bak(nums, startIndex):
        res.append(path[:])  # 在终止添加前, 收集子集，防止漏掉自己
        for i in range(startIndex, len(nums)): # 当startIndex大于数组长度, 循环也就结束了, 所以不需要终止条件
            path.append(nums[i])
            bak(nums, i + 1)  # 递归
            path.pop() # 回溯
    bak(nums, 0)
    return res


if __name__ == "__main__":
    print aa([1,2,3])
    print aa([0])
