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

# 本题没有组合数量要求, 仅总和限制, 递归没有层数限制, 只要选取的元素总和超过target就返回!
# 递归终止: sum大于target和sum等于target
# 单层for循环从startIndex开始
def aa(candidates, target):
    res, path = [], []
    def bak(candidates, target, sum, startIndex):
        if sum > target: return
        if sum == target: return res.append(path[:])
        for i in range(startIndex, len(candidates)):
            if sum + candidates[i] > target: return   # 终止遍历
            sum += candidates[i]
            path.append(candidates[i])
            bak(candidates, target, sum, i)
            sum -= candidates[i]  # 回溯
            path.pop() # 回溯
    candidates = sorted(candidates)
    bak(candidates, target, 0, 0)
    return res 


if __name__ == "__main__":
    print aa([2,3,6,7], 7)
    print aa([2,3,5], 8)
    print aa([2], 1)
