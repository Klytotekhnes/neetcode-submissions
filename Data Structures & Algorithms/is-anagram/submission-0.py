class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False            

        symbol_counter_1 = dict()
        symbol_counter_2 = dict()
        for x1, x2 in zip(s, t):
            if x1 in symbol_counter_1:
                symbol_counter_1[x1] += 1
            else:
                symbol_counter_1[x1] = 1

            if x2 in symbol_counter_2:
                symbol_counter_2[x2] += 1
            else:
                symbol_counter_2[x2] = 1

        return symbol_counter_1 == symbol_counter_2