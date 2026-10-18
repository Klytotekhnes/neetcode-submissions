class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        left_max[0] = 0
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        right_max = [0] * len(height)
        right_max[-1] = 0
        for j in range(len(height) - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j + 1])
        volume = 0
        for k in range(len(height)):
            if min(left_max[k], right_max[k]) > height[k]:
                volume += min(left_max[k], right_max[k]) - height[k]

        return volume

        