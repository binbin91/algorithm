# -*- coding: utf-8 -*-

def aa(nums, target):
    ans, n = [], len(nums)
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: continue
        for k in range(i+1, n):
            if k > i+1 and nums[k] == nums[k-1]: continue
            p, q = k + 1, n -1
            while p < q:
                total = nums[i] + nums[k] + nums[p] + nums[q]
                if total > target: 
                    q -= 1
                elif total < target: 
                    p += 1
                else:
                    ans.append([nums[i], nums[k], nums[p], nums[q]])
                    while p < q and nums[p] == nums[p+1]: p += 1
                    while p < q and nums[q] == nums[q-1]: q -= 1
                    p += 1
                    q -= 1
    return ans


if __name__ == "__main__":
    print aa([1,0,-1,0,-2,-2], 0)
