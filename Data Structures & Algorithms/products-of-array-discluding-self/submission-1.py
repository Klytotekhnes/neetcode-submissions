class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [None] * len(nums)
        prefix_product[0] = 1
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        suffix_product = [None] * len(nums)
        suffix_product[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

        ans = [None] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix_product[i] * suffix_product[i]

        return ans
