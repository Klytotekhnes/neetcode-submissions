class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        elif len(heights) == 0:
            return 0

        stack = []
        areas = []
        max_area = 0
        m = 0
        for n, h in enumerate(heights):
            m = n
            while stack and  h <= stack[-1][1]:
                area = stack[-1][1] * (n - stack[-1][0])
                max_area = max(max_area, area)
                m, _ = stack.pop()
            stack.append([m, h])
        for n, h in stack:
            area = h * (len(heights) - n)
            max_area = max(max_area, area)
        return max_area