# -*- coding: utf-8 -*-

import collections

# 哈希表
# 遍历字符串，统计字符串出现的个数
# 再遍历字符串，找出第一次个次数为1的字符，返回其位置即可
def aa(data):
    if not data: return - 1
    dic = collections.Counter(data)
    for k,v in enumerate(data):
        if dic[v] == 1:
            return k
    return -1

if __name__ == "__main__":
    data = "google" 
    print aa(data)
