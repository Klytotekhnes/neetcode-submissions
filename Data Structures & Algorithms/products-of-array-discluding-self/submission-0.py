class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1, 0]
        for num in nums:
            if num:
                product[0] *= num
            else:
                product[1] += 1
        
        if product[1] > 1:
            return [0] * len(nums)

        output = [None] * len(nums)
        for i in range(len(nums)):
            if nums[i]:
                if not product[1]:
                    output[i] = int(product[0] / nums[i])
                else:
                    output[i] = 0
            else:
                output[i] = product[0]
        return output