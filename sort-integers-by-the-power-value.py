class Solution:
    def findKthSmallest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x < pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        L, M = len(left), len(mid)
        if k <= L:
            return self.findKthSmallest(left, k)
        elif k > L + M:
            return self.findKthSmallest(right, k - L - M)
        else:
            return mid[0]
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        c = {}
        def getp(x):
            if x == 1:
                return 0
            if x in c:
                return c[x]
            c[x] = 1 + getp(x // 2) if x % 2 == 0 else 1 + getp(3 * x + 1)
            return c[x]
        return self.findKthSmallest([(getp(i), i) for i in range(lo, hi + 1)], k)[1]