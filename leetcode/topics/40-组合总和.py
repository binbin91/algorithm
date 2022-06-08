# -*- coding: utf-8 -*-

# Carl哥, 回溯三部曲
# 1. 递归函数参数
# 2. 递归终止条件
# 3. 单层搜索逻辑
#
# 组合问题、子集问题和分割问题都抽象为一棵树, 组合与分割都是收集树的叶子节点, 而子集是找树的所有节点
# 求组合:
#   若一个集合来求组合的话, 就需要startIndex; 
#   若多个集合取组合, 各个集合之间互不影响, 就不用startIndex
#   求组合与求组合总和区别: 1. 组合没有数量要求 2. 元素可无限重复选取 

# 与39区别, 集合有重复元素, 但还不能有重复组合(同一树层上使用过的去重, 树层去重需要对数组排序！！)
def aa(candidates, target):
    res, path = [], []
    def bak(candidates, target, sum, startIndex):
        if sum == target: res.append(path[:])
        for i in range(startIndex, len(candidates)):
            if sum + candidates[i] > target: return   # 终止遍历
            if i > startIndex and candidates[i] == candidates[i-1]: continue # 同树层使用过元素跳过
            sum += candidates[i]
            path.append(candidates[i])
            bak(candidates, target, sum, i+1)  # i+1, 每个数字在组合中只能使用一次
            sum -= candidates[i]  # 回溯
            path.pop() # 回溯
    candidates = sorted(candidates)
    bak(candidates, target, 0, 0)
    return res


if __name__ == "__main__":
    print aa([10,1,2,7,6,1,5], 8)
    print aa([2,5,2,1,2], 5)
