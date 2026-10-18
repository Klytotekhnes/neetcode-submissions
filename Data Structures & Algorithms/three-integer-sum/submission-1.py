class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []

        answer = set()
        for j in range(1, len(nums) - 1):
            i, k = 0, len(nums) - 1
            while i < j and j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.add((nums[i], nums[j], nums[k]))
                    i += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    i += 1
        return [list(x) for x in list(answer)]