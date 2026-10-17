class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while r > l:
            m = int((l + r) / 2)
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r = m - 1
        if target <= nums[-1]:
            l = r
            r = len(nums) - 1    
        else:
            l = 0
        while l <= r:
            m = int((l + r) / 2)
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        return -1

