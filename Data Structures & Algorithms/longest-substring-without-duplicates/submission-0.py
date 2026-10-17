class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        letters_set = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in letters_set:
                letters_set.remove(s[l])
                l += 1
            letters_set.add(s[r])
            longest = max(longest, r - l + 1)

        return longest