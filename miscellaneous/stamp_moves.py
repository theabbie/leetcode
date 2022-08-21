class Solution:
    def getPos(self, target, stamp):
        n = len(target)
        k = len(stamp)
        same = lambda a, b: b == '?' or a == b
        for i in range(n - k + 1):
            valid = True
            charseen = False
            for j in range(i, i + k):
                if target[j] != '?':
                    charseen = True
                if not same(stamp[j - i], target[j]):
                    valid = False
                    break
            if valid and charseen:
                yield i
                
    def minmoves(self, stamp, target):
        n = len(target)
        k = len(stamp)
        if target == ['?'] * n:
            return []
        minlen = float('inf')
        minres = None
        res = []
        for i in self.getPos(target, stamp):
            newtarget = target[:]
            for j in range(i, i + k):
                newtarget[i] = '?'
            curr = self.minmoves(stamp, newtarget)
            if len(curr) < minlen:
                minlen = len(curr)
                minres = i
                res = curr
        return [minres] + res
    
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = list(target)
        return self.minmoves(stamp, target)