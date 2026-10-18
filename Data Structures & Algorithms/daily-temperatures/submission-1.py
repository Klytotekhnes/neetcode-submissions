class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        for n, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                prev_n, _ = stack.pop()
                results[prev_n] = n - prev_n
            stack.append([n, t])

        return results