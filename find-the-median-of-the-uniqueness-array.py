class Solution:
    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res
    
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        beg = 1
        end = len(set(nums))
        res = end
        pos = ((n * (n + 1) // 2) - 1) // 2
        while beg <= end:
            mid = (beg + end) // 2
            l = self.atMostK(nums, mid - 1)
            r = self.atMostK(nums, mid)
            if l <= pos <= r - 1:
                res = mid
                break
            if pos < l:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res