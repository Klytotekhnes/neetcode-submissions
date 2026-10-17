class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_element:
            if val <= self.min_element[-1]:
                self.min_element.append(val)
        else:
            self.min_element.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_element[-1]:
            self.min_element.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element[-1]
        
