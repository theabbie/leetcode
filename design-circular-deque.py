class MyCircularDeque:
    def __init__(self, k: int):
        self.i = 0
        self.l = 0
        self.k = k
        self.q = [-1] * self.k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.l += 1
        self.i = (self.i + self.k - 1) % self.k
        self.q[self.i] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.l += 1
        self.q[(self.i + self.l + self.k - 1) % self.k] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.i = (self.i + 1) % self.k
        self.l -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.l -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.i]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.i + self.l + self.k - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.k