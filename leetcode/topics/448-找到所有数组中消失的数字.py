# -*- coding: utf-8 -*-


# 原地操作 
# 遍历数组, 计算前一个元素出现的次数(nums[i-]1 * -1), 若前一个元素已经是负数, 表明已存在则无需计算
# 最后遍历数组, 若元素大于0, 说明未出现过，就是我们要找的消失数字
def aa(nums):
    for i, n in enumerate(nums):
        if nums[abs(n)-1] > 0:
            nums[abs(n)-1] *= -1

    res = []
    for i in range(len(nums)):
        if nums[i] > 0: res.append(i+1)
    return res


if __name__ == "__main__":
    print aa([4,3,2,7,8,2,3,1])
    print aa([1,1])
