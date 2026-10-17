class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        for j in range(len(nums)):
            i, k = 0, len(nums) - 1
            while i < j and j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    answer.add((nums[i], nums[j], nums[k]))
                    i += 1
                    k -= 1
        return [list(x) for x in answer]