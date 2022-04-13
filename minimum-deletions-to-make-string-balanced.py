class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        minDel = float('inf')
        aTillNow = [0]
        for c in s:
            if c == 'a':
                aTillNow.append(aTillNow[-1] + 1)
            else:
                aTillNow.append(aTillNow[-1])
        for i in range(n + 1):
            currDel = i - 2 * aTillNow[i] + aTillNow[n]
            minDel = min(minDel, currDel)
        return minDel