# -*- coding: utf-8 -*-


# 快排
def aa(nums):
    i , zero, two = 0, -1, len(nums)
    while i < two:
        # 元素1纳入属于1的部分，右移继续遍历
        if nums[i] == 1:
            i += 1
        # 交换下标two前面一个元素
        elif nums[i] == 2:
            two -= 1
            nums[i], nums[two] = nums[two], nums[i]
        # 交换下标zero后面一个元素
        else:
            zero += 1
            nums[i], nums[zero] = nums[zero], nums[i]
            i += 1
    return nums


if __name__ == "__main__":
    print aa([2,0,2,1,1,0])
    print aa([2,0,1])
