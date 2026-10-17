class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = ['']
        for i in range(2 * n):
            while len(res[0]) <= i:
                x = res.pop(0)
                if x.count('(') < n:
                    res.append(x + '(')
                if x.count('(') > x.count(')'):
                    res.append(x + ')')
        return res
                