class Solution:
    def distinct(self, a, b, curr, rem):
        ctr = 0
        if rem == 1:
            return 1
        key = (a, curr, rem)
        if key in self.cache:
            return self.cache[key]
        for i in self.nvals[curr]:
            if i != a:
                ctr += self.distinct(b, i, i, rem - 1)
        self.cache[key] = ctr
        return ctr
    
    def distinctSequences(self, n: int) -> int:
        self.cache = {}
        ctr = 0
        self.nvals = {1: [2, 3, 4, 5, 6], 2: [1, 3, 5], 3: [1, 2, 4, 5], 4: [1, 3, 5], 5: [1, 2, 3, 4, 6], 6: [1, 5]}
        for i in range(1, 7):
            ctr += self.distinct(-1, i, i, n)
        return ctr % (10 ** 9 + 7)