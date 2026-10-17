import math


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while r - l > 1:
            m = math.ceil((l + r) / 2)
            if nums[m] < nums[l]:
                r = m
            elif nums[m] > nums[l]:
                l = m
            if r - l == 1:
                return min(nums[l], nums[r])
            
        return nums[r]