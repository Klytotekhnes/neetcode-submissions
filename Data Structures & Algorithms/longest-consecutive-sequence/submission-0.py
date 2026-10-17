class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        end_to_length = dict()
        start_to_length = dict()
        max_length = 0
        
        for n in nums:
            # print(n)
            # print(max_length)
            if start_to_length.get(n, False) and end_to_length.get(n, False):
                start_to_length[n - end_to_length[n] - 1] += 1 + start_to_length[n]
                end_to_length[n + start_to_length[n] + 1] += 1 + end_to_length[n]
                if start_to_length[n - end_to_length[n] - 1] > max_length:
                    max_length = start_to_length[n - end_to_length[n] - 1]
                del start_to_length[n]
                del end_to_length[n] 
            elif start_to_length.get(n, False):
                start_to_length[n - 1] = start_to_length[n] + 1
                end_to_length[n + 1 + start_to_length[n]] += 1
                if start_to_length[n - 1] > max_length:
                    max_length = start_to_length[n - 1]
                del start_to_length[n]
            elif end_to_length.get(n, False):
                end_to_length[n + 1] = end_to_length[n] + 1
                start_to_length[n - end_to_length[n] - 1] += 1
                if start_to_length[n - end_to_length[n] - 1] > max_length:
                    max_length = start_to_length[n - end_to_length[n] - 1]
                del end_to_length[n]
            else:
                start_to_length[n - 1] = start_to_length.get(n - 1, 1)
                end_to_length[n + 1] = end_to_length.get(n + 1, 1)
                max_length = max(max_length, start_to_length[n - 1])
            # print('#####')
            # print('start', start_to_length)
            # print('end', end_to_length)
            # print(max_length)
            # print('##########')
        
        return max_length
