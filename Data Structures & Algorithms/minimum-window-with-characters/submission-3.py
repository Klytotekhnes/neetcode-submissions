class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        target = {}
        curr = {}
        ans = s + '_'
        for i in range(len(t)):
            target[t[i]] = 1 + target.get(t[i], 0)
            curr[s[i]] = 1 + curr.get(s[i], 0)
        if curr == target:
            return s[:len(t)]
        l = 0
        for r in range(len(t), len(s)):
            curr[s[r]] = 1 + curr.get(s[r], 0)
            while curr.get(s[l], 0) > target.get(s[l], 0):
                curr[s[l]] -= 1
                # if not curr[s[l]]:
                #     del curr[s[l]]
                l += 1
                if l > r:
                    break
            if not False in [curr.get(key, 0) >= target[key] for key in target.keys()]:
                if r - l + 1 < len(ans):
                    ans = s[l:r + 1]
        return '' if ans == s + '_' else ans
