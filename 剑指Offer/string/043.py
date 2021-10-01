# -*- coding: utf-8 -*-

# 切片
def aa(data, k):
    return data[k:] + data[:k]

# 原地反转
# 反转前半部分 -> 反转后半部分 -> 整体反转
def bb(data, k):
    if not data: return data
    
    data = list(data)
    def reverse(start, end):
        while start < end:
            data[start], data[end] = data[end], data[start]
            start += 1
            end -= 1

    reverse(0, k-1)
    reverse(k, len(data)-1)
    reverse(0, len(data)-1)
    return ''.join(data)

if __name__ == "__main__":
    data = "abcXYZdef"
    print aa(data, 3)
    print bb(data, 3)
