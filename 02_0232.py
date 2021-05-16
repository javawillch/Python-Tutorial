class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        return self.items.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.items[0]

    def empty(self) -> bool:
        bool = False if self.items else True
        return bool


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(13)
obj.push(1)
obj.push(123)
obj.push(111343)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
