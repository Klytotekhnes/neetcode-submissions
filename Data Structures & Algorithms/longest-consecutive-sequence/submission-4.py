class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        possible_start = set()
        for num in nums:
            if num + 1 in nums_set and num - 1 not in nums_set:
                possible_start.add(num)
        
        if len(possible_start) == 0:
            return 1

        max_count = 0
        for num in possible_start:
            count = 1
            k = num
            while k + 1 in nums_set:
                count += 1
                k += 1
            max_count = max(count, max_count)

        return max_count