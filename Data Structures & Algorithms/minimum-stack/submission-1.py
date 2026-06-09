class MinStack:
    def __init__(self):
        self.stack=[]
        self.minStack=[] # Idea:
        # If new Value newest smallest, add it
        # If new Value not smallest => keep adding smallest
        # When popping, always pop the latest in minStack as well

    def push(self, val: int) -> None:
        self.stack.append(val)
        smallest=val
        if self.minStack and self.minStack[-1]<smallest:
            smallest=self.minStack[-1]
        self.minStack.append(smallest)

    def pop(self) -> None:
        self.stack=self.stack[:-1]
        self.minStack=self.minStack[:-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
