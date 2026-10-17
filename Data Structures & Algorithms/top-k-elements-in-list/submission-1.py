class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:            
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        boundery = len(nums)
        answer = []
        for key, value in freq.items():
            if len(answer) < k:
                answer.append([key, value])
                boundery = min(boundery, value)

            elif value >= boundery:
                for i in range(k):
                    if answer[i][1] == boundery:
                        answer[i] = [key, value]
                        break
                boundery = min([x[1] for x in answer])
        
        return [x[0] for x in answer]