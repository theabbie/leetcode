from collections import defaultdict

class MyCalendarThree:
    def __init__(self):
        self.tree = defaultdict(lambda: [0, 0])
        self.M = 10 ** 9 + 1
    
    def update(self, root, start, end, pos, val):
        if start == end:
            self.tree[root][0] += val
            return
        mid = (start + end) // 2
        if pos <= mid:
            self.update(2 * root, start, mid, pos, val)
        else:
            self.update(2 * root + 1, mid + 1, end, pos, val)
        self.tree[root][0] = self.tree[2 * root][0] + self.tree[2 * root + 1][0]
        self.tree[root][1] = max(self.tree[2 * root][1], self.tree[2 * root][0] + self.tree[2 * root + 1][1])

    def book(self, start: int, end: int) -> int:
        self.update(1, 0, self.M, start, 1)
        self.update(1, 0, self.M, end, -1)
        return self.tree[1][1]