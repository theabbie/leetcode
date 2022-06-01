class Solution:
    def countUnique(self, n, used, first):
        if n == 0:
            return 0
        ctr = 0
        beg = 0
        if first:
            beg = 1
        for i in range(beg, 10):
            if i not in used:
                ctr += 1 + self.countUnique(n - 1, used.union({i}), False)
        return ctr
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return self.countUnique(n, set(), True) + 1