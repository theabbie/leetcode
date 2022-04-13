class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        l = len(n)
        for i in range(1, l):
            if i % 3 == 0:
               n = n[ : l - i] + '.' + n[l - i : ]
        return n