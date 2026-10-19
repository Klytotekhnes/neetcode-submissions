class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        
        def canEatAll(rate: int) -> bool:
            h_demand = 0
            for pile in piles:
                h_demand += math.ceil(pile / rate)
            return h_demand <= h

        if len(piles) == 0 or len(piles) > h:
            return None

        l, r = 1, max(piles)
        while l < r:
            m = int((l + r) / 2)
            if canEatAll(m):
                r = m
            else:
                l = m + 1

        return r