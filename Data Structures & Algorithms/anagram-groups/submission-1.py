class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group2string = {}
        for string in strs:
            counter = [0] * 30
            for s in string:
                counter[ord(s) - ord("a")] += 1
            prev_item = group2string.get(tuple(counter), [])
            prev_item.append(string)
            group2string[tuple(counter)] = prev_item

        return list(group2string.values())