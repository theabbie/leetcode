class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i = 0
        j = 0
        ctr = {}
        mlen = 0
        while i <= j and j < n:
            ctr[fruits[j]] = ctr.get(fruits[j], 0) + 1
            j += 1
            if len(ctr) <= 2:
                mlen = max(mlen, j - i)
            else:
                while len(ctr) > 2 and i < j:
                    ctr[fruits[i]] -= 1
                    if ctr[fruits[i]] == 0:
                        del ctr[fruits[i]]
                    i += 1
        return mlen