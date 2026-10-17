class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counter = set()
        for n in nums:
            if n in num_counter:
                return True
            else:
                num_counter.add(n)

        return False