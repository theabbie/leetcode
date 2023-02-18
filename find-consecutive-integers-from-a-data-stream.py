from collections import deque

class DataStream:
    def __init__(self, value: int, k: int):
        self.q = deque()
        self.value = value
        self.k = k
        self.diffctr = 0

    def consec(self, num: int) -> bool:
        self.q.appendleft(num)
        if num != self.value:
            self.diffctr += 1
        if len(self.q) > self.k:
            v = self.q.pop()
            if v != self.value:
                self.diffctr -= 1
        return len(self.q) >= self.k and self.diffctr == 0