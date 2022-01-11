# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

# 单词=物品, 字符串s=背包, 单词能否组成字符串s, 就是问物品能不能把背包装满
def aa(s, wordDict):
    # dp数组, 可以拆分为1个或多个在字典中出现的单词为dp[i]
    dp = [False] * (len(s) + 1) 
    dp[0] = True
    # 两种遍历都可以
    # 因本题要求子串, So先遍历背包, 再遍历物品
    for j in range(1, len(s)+1):
        for w in wordDict:
            if j >= len(w):
                dp[j] = dp[j] or (dp[j-len(w)] and w == s[j-len(w):j])  # 递推公式
    return dp[len(s)]


if __name__ == "__main__":
    print aa("leetcode", ["leet", "code"])
