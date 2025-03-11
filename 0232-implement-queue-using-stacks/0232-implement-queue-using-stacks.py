class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.front.append(x)

    def pop(self) -> int:
        if self.back:
            return self.back.pop()
        else:
            while self.front:
                self.back.append(self.front.pop())
            return self.back.pop()


    def peek(self) -> int:
        if self.back:
            return self.back[-1]
        else:
            while self.front:
                self.back.append(self.front.pop())
            return self.back[-1]

        

    def empty(self) -> bool:
        if self.front or self.back:
            return False
        else:
            return True

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()