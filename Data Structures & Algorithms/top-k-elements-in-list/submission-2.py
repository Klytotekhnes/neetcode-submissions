class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}
        freq = {}
        for el in nums:
            if el in freq:
                buckets[freq[el]].remove(el)
                freq[el] += 1
            else:
                freq[el] = 1

            if freq[el] in buckets:
                buckets[freq[el]].append(el)
            else:
                buckets[freq[el]] = [el]
        answer = []
        for i in range(len(nums), 0, -1):
            if i in buckets:
                answer.extend(buckets[i])
            if len(answer) == k:
                return answer
            