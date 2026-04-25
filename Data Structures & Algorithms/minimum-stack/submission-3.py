class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        temp = []
        if self.min:
            if self.min[-1] < val:
                for i in range(len(self.min)):
                    if self.min[-1] < val:
                        temp.append(self.min.pop())
                self.min.append(val)
                for i in temp[::-1]:
                    self.min.append(i)
            else:
                self.min.append(val)
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.min.remove(self.stack.pop())
        # print(self.min)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
