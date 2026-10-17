class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)) + "#")
            res.append(string)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        length = ''
        while i < len(s):
            if s[i] == '#':
                l = int(length)
                res.append(s[i + 1: i + l + 1])
                i = i + l + 1
                length = ''
            else:
                length += s[i]
                i += 1
        return res