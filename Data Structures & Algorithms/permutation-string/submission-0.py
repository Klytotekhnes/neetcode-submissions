class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # baseline =
        target = {}
        for s in s1:
            target[s] = target.get(s, 0) + 1
        l = 0
        curr = {}
        for r in range(len(s2)):
            curr[s2[r]] = curr.get(s2[r], 0) + 1
            while curr.get(s2[r], 0) > target.get(s2[r], 0):
                curr[s2[l]] -= 1
                if curr[s2[l]] == 0:
                  del curr[s2[l]]
                l += 1
            if curr == target:
                return True
        return False 
