class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.k = k
        self.i = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[(self.i + self.size) % self.k] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.i] = None
        self.i = (self.i + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.i]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.k + self.i + self.size - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k