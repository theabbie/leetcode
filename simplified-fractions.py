class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def simplifiedFractions(self, n: int) -> List[str]:
        op = set()
        for j in range(1, n + 1):
            for i in range(1, j):
                mul = self.gcd(i, j)
                op.add("{}/{}".format(i // mul, j // mul))
        return op