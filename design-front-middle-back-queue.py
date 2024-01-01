from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.l = deque()
        self.r = deque()
        
    def empty(self):
        return len(self.l) == 0 and len(self.r) == 0
    
    def balance(self):
        while len(self.r) < len(self.l):
            self.r.appendleft(self.l.pop())
        while len(self.r) - len(self.l) > 1:
            self.l.append(self.r.popleft())

    def pushFront(self, val: int) -> None:
        self.l.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        self.l.append(val)
        self.balance()

    def pushBack(self, val: int) -> None:
        self.r.append(val)
        self.balance()

    def popFront(self) -> int:
        if self.empty():
            return -1
        res = -1
        if len(self.l) == 0:
            res = self.r.popleft()
        else:
            res = self.l.popleft()
        self.balance()
        return res

    def popMiddle(self) -> int:
        if self.empty():
            return -1
        if len(self.r) > len(self.l):
            res = self.r.popleft()
        else:
            res = self.l.pop()
        self.balance()
        return res

    def popBack(self) -> int:
        if self.empty():
            return -1
        res = self.r.pop()
        self.balance()
        return res