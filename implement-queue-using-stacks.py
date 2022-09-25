class MyQueue:
    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        self.peek()
        return self.b.pop()

    def peek(self) -> int:
        if len(self.b) == 0:
            while len(self.a) > 0:
                self.b.append(self.a.pop())
        return self.b[-1]

    def empty(self) -> bool:
        return len(self.a) + len(self.b) == 0