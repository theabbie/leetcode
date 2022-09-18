class StockSpanner:
    def __init__(self):
        self.stack = []
        self.ctr = 0

    def next(self, price: int) -> int:
        while len(self.stack) > 0 and price >= self.stack[-1][1]:
            self.stack.pop()
        res = -1
        if len(self.stack) > 0:
            res = self.stack[-1][0]
        self.stack.append((self.ctr, price))
        self.ctr += 1
        return self.ctr - res - 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)