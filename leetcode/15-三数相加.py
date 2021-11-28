# -*- coding: utf-8 -*-

def aa(nums):
    ans, n = [], len(nums)
    nums.sort()
    for i in range(n):
        l, r = i + 1, n -1
        if nums[i] > 0: break
        if i >= 1 and nums[i] == nums[i-1]: continue
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total > 0: 
                r -= 1
            elif total < 0: 
                l += 1
            else:
                ans.append([nums[i], nums[l], nums[r]])
                while l != r and nums[l] == nums[l+1]: l += 1
                while l != r and nums[r] == nums[r-1]: r -= 1
                l += 1
                r -= 1
    return ans


if __name__ == "__main__":
    print aa([-1,0,1,2,-1,-4])
