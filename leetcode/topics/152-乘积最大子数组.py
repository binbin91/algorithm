# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组

def aa(nums):
    imax = imin = res = nums[0] 
    for i in range(1, len(nums)):
        # 递推公式, 遍历数组计算最大值imax和最小值imin
        mx, mi = imax, imin
        imax = max(mx * nums[i], mi * nums[i], nums[i])
        imin = min(mx * nums[i], mi * nums[i], nums[i])
        res = max(res, imax)
    return res


if __name__ == "__main__":
    print aa([2, 3, -2, 4])
    print aa([-2, 0, -1])
