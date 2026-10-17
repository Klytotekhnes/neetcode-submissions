from math import ceil


class Solution:
    @staticmethod
    def demandTime(piles: List[int], k: int) -> int:
        time = 0
        for pile in piles:
            time += int(ceil(pile / k))
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        while self.demandTime(piles, k) > h:
            k *= 2

        l, r = k // 2, k
        while l < r:
            k = int((l + r) / 2)
            if k == r or k == l:
                return r
            if self.demandTime(piles, k) > h:
                l = k
            elif self.demandTime(piles, k) <= h:
                r = k
        
            
        