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

# map定义一个数字与字母映射关系
# 递归参数digits和index(用于记录遍历第几个数字了, 同时表示树的深度)
# 若index等于输入digits长度, 收集结果并结束本层递归
# 获取index指向的数字, 并从映射关系中找到对应字符集，然后循环处理

class Solution:
    def __init__(self):
        self.ans = []
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits):
        self.ans = []
        if not digits: return []
        self.bak(digits, 0, '')
        return self.ans
   
    def bak(self, digits, idx, ans):
        if idx == len(digits):
            self.ans.append(ans)
            return
        ls = self.letter_map[digits[idx]]
        for l in ls:
            self.bak(digits, idx+1, ans + l)
    

if __name__ == "__main__":
    print Solution().letterCombinations("23") 
