class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            while queue and nums[r] >= nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if r >= k - 1:
                res.append(nums[queue[0]])
                l += 1    

        return res    
