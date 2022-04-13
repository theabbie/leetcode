class Solution:
    def cvow(self, n):
        if n == 1:
            return [5, 4, 3, 2, 1]
        curr = self.cvow(n - 1)
        op = [curr[-1]]
        for i in range(3, -1, -1):
            op.append(op[-1] + curr[i])
        return op[::-1]
    
    def countVowelStrings(self, n: int) -> int:
        return self.cvow(n)[0]