class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reverse = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for bracket in s:
            if bracket in ['(', '[', '{']:
                stack.append(bracket)
            else:
                if stack and stack[-1] == reverse[bracket]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True