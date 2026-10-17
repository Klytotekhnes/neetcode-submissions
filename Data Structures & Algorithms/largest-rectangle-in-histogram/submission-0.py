class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_volume = 0
        max_heights = max(heights)
        volumes = [0] * max_heights
        for h in heights:
            for i in range(max_heights):
                if i < h:
                    volumes[i] += (i + 1)
                    max_volume = max(max_volume, volumes[i])
                else:
                    volumes[i] = 0
        return max_volume