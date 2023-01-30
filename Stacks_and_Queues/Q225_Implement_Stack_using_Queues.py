class MyStack:

    def __init__(self):
        self.L = []

    def push(self, x: int) -> None:
        self.L.append(x)

    def pop(self) -> int:
        for i in range(len(self.L)-1):
            x = self.L.pop(0)
            self.L.append(x)
        return self.L.pop(0)

    def top(self) -> int:
        return self.L[len(self.L)-1]

    def empty(self) -> bool:
        return len(self.L)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
