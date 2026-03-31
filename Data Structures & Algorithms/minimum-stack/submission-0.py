class MinStack:

    def __init__(self):
        self.a = []
        self.m = []

    def push(self, val: int) -> None:
        self.a.append(val)
        val = min(val, self.m[-1] if self.m else val)
        self.m.append(val)
        
    def pop(self) -> None:
        self.a.pop()
        self.m.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.m[-1]

#TC: O(1)
#Sc: O(n)
        
