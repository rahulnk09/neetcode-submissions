class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini=min(self.mini,val)
    def pop(self) -> None:
        if self.mini != self.stack[-1]:
            self.stack.pop()
        else:
            self.stack.pop()
            if self.stack:
                self.mini=min(self.stack)
            else:
                self.mini=float('inf')
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.mini