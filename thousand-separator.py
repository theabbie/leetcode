class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        l = len(n)
        if l <= 3:
            return n
        for i in range(l):
            if i > 0 and i % 3 == 0:
               n = n[ : l - i] + '.' + n[l - i : ]
        return n