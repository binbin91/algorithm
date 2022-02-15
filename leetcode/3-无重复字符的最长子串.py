# -*- coding: utf-8 -*-

def aa(s):
    cur, res = [], 0
    for i in range(len(s)):
        while s[i] in cur: cur.pop(0)  # 左出
        cur.append(s[i])  # 右进
        # print cur, res输出
        # ['a'], 0
        # ['a', 'b'], 1
        # ['a', 'b', 'c'], 2
        # ['b', 'c', 'a'], 3
        # ['c', 'a', 'b'], 3
        # ['a', 'b', 'c'], 3
        # ['c', 'b'], 3
        # ['b'], 3
        res = max(res, len(cur))
    return res


if __name__ == "__main__":
    print aa("abcabcbb")
