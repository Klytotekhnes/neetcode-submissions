class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = [0] * (ord('Z') - ord('A') + 1) 
        baseline = ord('A')
        main_char = 0
        length = 0
        for r in range(len(s)):
            counts[ord(s[r]) - baseline] += 1
            main_char = max(counts)
            while sum(counts) - main_char > k:
                counts[ord(s[l]) - baseline] -= 1
                l += 1
                main_char = max(counts)
            length = max(length, sum(counts))            
            
        return length
            