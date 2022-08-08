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

# 和77不同的是, 整个集合是已经固定[1...9]
# 增加一个sum用于记录已收集元素总和(path长度)
# 剪枝: sum > n, 已收集元素总和大于n, 往后遍历无意义了, 直接剪掉;

def aa(k, n):
    res, path = [], []
    def recur(n, k, sum, s):
        if sum > n: return
        if sum == n and len(path) ==k: 
            res.append(path[:])
        for i in range(s, 9-(k-len(path))+2):
            path.append(i)
            sum += i
            recur(n, k, sum, i+1)
            sum -= i
            path.pop()
    recur(n, k, 0, 1)
    return res 
