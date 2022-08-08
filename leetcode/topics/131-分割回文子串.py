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

# 若idx等于s长度, 说明已找到分割子串, 放入结果集合里并结束递归
# 递归时通过[idx:i+1]获取要截取的子串, 然后判断子串是否回文(正序和反序相同, 就是回文串), 是放入path

class Solution:
    def __init__(self):
        self.path, self.res = [], []

    def partition(self, s):
        self.path, self.res = [], []
        self.bak(s, 0)
        return self.res
   
    def bak(self, s, idx):
        if idx == len(s):
            self.res.append(self.path[:])
            return

        for i in range(idx, len(s)):
            tmp = s[idx:i+1]
            if tmp == tmp[::-1]:
                self.path.append(tmp)
                self.bak(s, i+1)
                self.path.pop()
            else:
                continue
    

if __name__ == "__main__":
    print Solution().partition("aab") 
