# -*- coding: utf-8 -*-


def partition(nums, left, right):
    pivot = nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]
    nums[i] = pivot
    return i

# 快排
def quicksort(nums, l, r):
    if l < r:
        idx = partition(nums, l, r)
        quicksort(nums, l, idx-1)
        quicksort(nums, idx+1, r)
        return nums

# 寻找到第k个数, 使得nums数组中idx左边是前k个小的数, 右边是后面n-k个大的数
def topk_split(nums, k, left, right):
    if left < right:
        idx = partition(nums, left, right)
        if idx == k: return
        elif idx < k: topk_split(nums, k, idx+1, right)
        else: topk_split(nums, k, left+1, idx-1)

# 获得前k小的数
def topk_smalls(nums, k):
    topk_split(nums, k, 0, len(nums)-1)
    return nums[:k]

# 获得第k小的数
def topk_small(nums, k):
    topk_split(nums, k, 0, len(nums)-1)
    return nums[k-1]

# 获得前k大的数
def topk_larges(nums, k):
    topk_split(nums, len(nums)-k, 0, len(nums)-1)
    return nums[len(nums)-k:]

# 获得第k大的数
def topk_large(nums, k):
    topk_split(nums, len(nums)-k, 0, len(nums)-1)
    return nums[len(nums)-k]

# 排序前k个小的数
def topk_sort_left(nums, k):
    topk_split(nums, k, 0, len(nums)-1)
    topk = nums[:k]
    quicksort(topk, 0, len(topk)-1)
    return topk+nums[k:]

# 排序后k个大的数
def topk_sort_right(nums, k):
    topk_split(nums, len(nums)-k, 0, len(nums)-1)
    topk = nums[len(nums)-k:]
    quicksort(topk, 0, len(topk)-1)
    return nums[:len(nums)-k]+topk


if __name__ == "__main__":
    #arr = [1,3,2,2,0]
    #print quicksort(arr, 0, len(arr)-1)
    #arr = [1,3,2,3,0,-19]
    #print topk_smalls(arr, 2)
    #print topk_small(arr, 3)
    #print topk_small(arr, 3)
    #print topk_larges(arr, 3)
    #print topk_large(arr, 2)
    #arr = [0,0,1,3,4,5,0,7,6,7]
    #print topk_sort_left(arr, 4)
    arr = [0,0,1,3,4,5,0,-7,6,7]
    print topk_sort_right(arr, 4)
