class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L, R = 0, len(s) - 1
        while L < R:
            if not s[R].isalpha() and not s[R].isdigit():
                R -= 1
                continue
            if not s[L].isalpha() and not s[L].isdigit():
                L += 1
                continue
            if s[R] != s[L]:
                return False
            else:
                R -= 1
                L += 1
        return True