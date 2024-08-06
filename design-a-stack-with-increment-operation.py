from collections import Counter

class CustomStack:
    def __init__(self, maxSize: int):
        self.s = []
        self.increments = Counter()
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.s) == self.maxSize:
            return -1
        self.s.append(x)

    def pop(self) -> int:
        if len(self.s) == 0:
            return -1
        self.s[-1] += self.increments[len(self.s)]
        self.increments[len(self.s) - 1] += self.increments[len(self.s)]
        del self.increments[len(self.s)]
        return self.s.pop()

    def increment(self, k: int, val: int) -> None:
        self.increments[min(k, len(self.s))] += val