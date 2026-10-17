class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        water_level = [0] * len(height)
        limit = height[0]
        for l in range(len(height)):
            if height[l] <= limit:
                water_level[l] = limit - height[l]
            else:
                limit = height[l]
        
        limit = height[-1]
        for r in range(len(height) - 1, 0, -1):
            if height[r] <= limit:
                water_level[r] = min(limit - height[r], water_level[r])
            else:
                limit = height[r]
                water_level[r] = 0

        return sum(water_level)
