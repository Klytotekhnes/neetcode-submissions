class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inverse = {'(': ')',
                   '[': ']',
                   '{': '}'}
        for symbol in s:
            if symbol in ['(', '{', '[']:
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if symbol != inverse[last]:
                    return False
        return not stack
