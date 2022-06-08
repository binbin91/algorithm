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

# n相当于树的宽度, k相当于树的深度
# 每次从集合中选取元素, 可选择的范围随着选择的进行而收缩, 调整可选择的范围, 就是要靠startIndex
# 递归终止: 若path数组大小等于k, 说明我们找到了一个子集大小为k的组合
# for循环每次从startIndex开始遍历, 然后用path数组保存取到的节点
def aa(n, k):
    res, path = [], []
    def bak(n, k, startIndex):
        if len(path) == k: 
            res.append(path[:])
            return
        for i in range(startIndex, n-(k-len(path))+2):
            path.append(i)
            bak(n, k, i+1)
            path.pop()
    bak(n, k, 1)
    return res 


if __name__ == "__main__":
    print aa(4, 2)
    print aa(1, 1)
