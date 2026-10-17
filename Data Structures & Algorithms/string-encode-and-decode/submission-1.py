class Solution:

    def encode(self, strs: List[str]) -> str:
        result = [str(len(strs))]
        result.extend([str(len(x)) for x in strs])
        
        return '_'.join(result) + '_' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        counter = 0
        num = []
        for symbol in s:
            if symbol == '_':
                break
            else:
                num.append(symbol)
        num = int(''.join(num))
        s_split = s.split('_')
        nums = [int(x) for x in s_split[1:num + 1]]
        start_index = 0
        for symbol in s:
            start_index += 1
            if counter == (num + 1):
                break
            
            elif symbol == '_':
                counter += 1
        start_index -= 1
        strs = []
        for i in range(num):
            strs.append(s[start_index:start_index+nums[i]])
            start_index += nums[i]

        return strs
