# -*- coding: utf-8 -*-

# Carl哥, 回溯三部曲
# 1. 递归函数参数
# 2. 递归终止条件
# 3. 单层搜索逻辑

# 组合问题、子集问题和分割问题都抽象为一棵树, 组合与分割都是收集树的叶子节点, 而子集恶事找树的所有节点

# 1，排列是有序的, [1,2]和[2,1]是两个集合
# 2. 当收集元素数组path大小和nums数组一样大的时候，说明找到一个全排列, 也表示到达叶子节点
#.3. 排列问题, 每次都从头开始搜索, 例如元素1在[1,2]中已使用过, 但是在[2,1]中还要再使用一次

# 排列问题不同:
# 1. 每次都是从0开始搜索而不是startIndex
# 2. 需要used数组记录path里都放了哪些元素
def aa(nums):
    # res存放符合条件结果的集合, path用来存放符合条件的结果
    res, path = [], [] 
    def bak(nums):
        if len(path) == len(nums):
            return res.append(path[:]) # 已找一个全排列
    
        for i in range(len(nums)):
            if nums[i] in path: continue # path已存放的元素, 则直接跳过
            path.append(nums[i])
            print path
            bak(nums)  # 递归
            path.pop() # 回溯
    bak(nums)
    return res


if __name__ == "__main__":
    print #aa([1,2,3])
    print aa([0,1])
    print #aa([1])
