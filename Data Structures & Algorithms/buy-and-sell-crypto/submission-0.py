class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_benefit = 0
        for r in range(len(prices)):
            max_benefit = max(max_benefit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        return max_benefit