# -*- coding: utf-8 -*-

def aa(nums):
    def merge_sort(l, r):
        if l >= r: return 0
        m = (l + r) // 2
        res = merge_sort(l, m) + merge_sort(m + 1, r)
        i, j = l, m + 1
        tmp[l:r + 1] = nums[l:r + 1]
        for k in range(l, r + 1):
            if i == m + 1:
                nums[k] = tmp[j]
                j += 1
            elif j == r + 1 or tmp[i] <= tmp[j]:
                nums[k] = tmp[i]
                i += 1
            else:
                nums[k] = tmp[j]
                j += 1
                res += m - i + 1 # 统计逆序对
        return res
        
    tmp = [0] * len(nums)
    return merge_sort(0, len(nums) - 1)


if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,0] 
    print aa(array)
