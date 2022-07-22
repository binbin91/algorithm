# -*- coding: utf-8 -*-

# 题目要求, 每隔2k个字符的前k个字符反转, 若剩余字符少于k个, 需要将剩余字符整体反转
# 解题思路
# 利用for循环表达式特性(start, end, step)来确定需要调换的初始位置
# 切片替换, 非一个个字符串替换


def aa(s, k):
    ss = [i for i in s]
    n = len(s)
    for i in range(0, n, 2*k):
        ss[i:i+k] = ss[i:i+k][::-1]
    return "".join(ss)


if __name__ == "__main__":
    print aa("abcdefg", 2)
