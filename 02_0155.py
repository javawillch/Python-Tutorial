class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return min(self.items)


# # Your MinStack object will be instantiated and called as such:
# val = 100
# obj = MinStack()
# obj.push(100)
# obj.push(22)
# obj.push(300)
# obj.push(39999)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# print(param_3)
# print(param_4)