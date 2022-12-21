class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        p = sum(arr)
        msum = 0
        mending = 0
        for el in arr:
            mending = max(el, el + mending)
            msum = max(msum, mending)
        if k > 1:
            mpref = 0
            msuff = 0
            pf = sf = 0
            for i in range(n):
                pf += arr[i]
                sf += arr[n - i - 1]
                mpref = max(mpref, pf)
                msuff = max(msuff, sf)
            msum = max(msum, max(p, 0) * (k - 2) + mpref + msuff)
        return msum % (10 ** 9 + 7)