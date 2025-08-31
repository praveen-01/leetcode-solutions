class MinStack:

    def __init__(self):
        self.mini = float("inf")
        self.st = []
        
    def push(self, val: int) -> None:
        if self.mini>val:
            self.mini = val
        self.st.append([val,self.mini])
        
    def pop(self) -> None:
        temp = self.st.pop(-1)
        if self.mini == temp[1]:
            if self.st:
                self.mini = self.st[-1][1]
            else:
                self.mini = float("inf")

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.mini
