from collections import Counter

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        ctr = Counter(deck)
        l = 0
        for el in ctr:
            l = self.gcd(l, ctr[el])
        return l > 1