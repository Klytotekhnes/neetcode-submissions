class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_index = {}
        
        for i in range(len(nums)):
            if nums[i] in diff_index:
                return [diff_index[nums[i]], i]
            else:
                diff_index[target - nums[i]] = i 