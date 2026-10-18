class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                second_term = stack.pop()
                first_term = stack.pop()
                if token == '*':
                    res = first_term * second_term
                elif token == '/':
                    res = int(float(first_term) / second_term)
                elif token == '+':
                    res = first_term + second_term
                elif token == '-':
                    res = first_term - second_term
                stack.append(res)

        return stack.pop()