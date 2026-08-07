class MinStack:

    def __init__(self):
        self.stack=[]
        self.minn=[]

    def push(self, val: int) -> None:
        if not self.minn:
            self.minn.append(val)
        else:
            self.minn.append(min(self.minn[-1],val))
        return self.stack.append(val)


    def pop(self) -> None:
        self.minn.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1]