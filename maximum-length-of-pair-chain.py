class Solution:
    def biggestChain(self, pairs, i, n):
        if i == n - 1:
            return 1
        if i in self.cache:
            return self.cache[i]
        mlen = 1
        for j in range(i+1, n):
            if pairs[j][0] > pairs[i][1]:
                curr = self.biggestChain(pairs, j, n)
                mlen = max(mlen, 1 + curr)
        self.cache[i] = mlen
        return mlen
    
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[0])
        self.cache = {}
        n = len(pairs)
        mlen = 1
        for i in range(n):
            curr = self.biggestChain(pairs, i, n)
            mlen = max(mlen, curr)
        return mlen