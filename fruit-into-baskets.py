from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i = 0
        ctr = Counter()
        mlen = 0
        for j in range(n):
            ctr[fruits[j]] += 1
            if len(ctr) <= 2:
                mlen = max(mlen, j - i + 1)
            else:
                while i < j and len(ctr) > 2:
                    ctr[fruits[i]] -= 1
                    if ctr[fruits[i]] == 0:
                        del ctr[fruits[i]]
                    i += 1
                if len(ctr) <= 2:
                    mlen = max(mlen, j - i + 1)
        return mlen