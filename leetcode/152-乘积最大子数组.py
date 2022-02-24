# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(nums):
    imax, imin, res = 1, 1, float("-inf")
    for n in nums:
        # 递推公式, 遍历数组计算最大值imax和最小值imin
        imax = max(imax * n, imin * n, n)
        imin = min(imax * n, imin * n, n)
        res = max(res, imax)
    return res


if __name__ == "__main__":
    print aa([2, 3, -2, 4])
    print aa([-2, 0, -1])
