class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # value = int(tokens.pop(0))
        stack = []
        while tokens:
            x = tokens.pop(0)
            if x not in ['+', '-', '*', '/']:
                stack.append(int(x))
            else:
                second_term = stack.pop()
                first_term = stack.pop()
                
                if x == '+':
                    stack.append(first_term + second_term)
                elif x == '-':
                    stack.append(first_term - second_term)
                elif x == '*':
                    stack.append(first_term * second_term)
                else:
                    # stack.append(abs(first_term) // abs(second_term))
                    stack.append(int(first_term / second_term))
        return stack[0]