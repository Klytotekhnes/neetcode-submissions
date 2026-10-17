class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [0] * 30
        t_list = [0] * 30
        for symbol in s:
            s_list[ord(symbol) - ord("a")] += 1
        for symbol in t:
            t_list[ord(symbol) - ord("a")] += 1

        if s_list == t_list:
            return True
        return False