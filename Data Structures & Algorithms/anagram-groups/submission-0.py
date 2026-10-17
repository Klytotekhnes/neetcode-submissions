class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_to_freq = {}
        for string in strs:
            string_to_freq[string] = {}
            for symbol in string:
                string_to_freq[string][symbol] = 1 + string_to_freq[string].get(symbol, 0)
        
        answer = [[strs[0]]]
        for string in strs[1:]:
            flag_success = False
            for group in answer:
                if string_to_freq[string] == string_to_freq[group[0]]:
                    group.append(string)
                    flag_success = True
                    break
            
            if not flag_success:
                answer.append([string])

        return answer
