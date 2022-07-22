# -*- coding: utf-8 -*-

# 双指针解法
# 一个指针在字符串头部, 一个指针在字符串尾部, 俩指针同时向中间移动并交换元素 


def aa(s):
    l, r = 0, len(s)-1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


if __name__ == "__main__":
    print aa(["h","e","l","l","o"])
