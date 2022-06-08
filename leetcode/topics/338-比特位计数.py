# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组


def aa(n):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i>>1] + (i & 1)
    return res


if __name__ == "__main__":
    print aa(2)
    print aa(5)
