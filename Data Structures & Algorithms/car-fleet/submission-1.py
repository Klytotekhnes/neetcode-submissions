class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda x: x[0])
        stack = []
        for p, s in pos_speed:
            time_to_finish = (target - p) / s
            while stack and stack[-1] <= time_to_finish:
                stack.pop()
            stack.append(time_to_finish)
        return len(stack)