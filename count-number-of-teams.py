class Solution:
    def count(self, nums, r):
        n = len(nums)
        B = 10
        res = [0] * n
        MASK = 0
        p = 1 << B
        od = sorted(range(n), reverse = r)
        for b in range(B, -1, -1):
            ctr = defaultdict(lambda: [0, 0])
            for i in od:
                if bool(nums[i] & (1 << b)) != bool(r):
                    res[i] += ctr[nums[i] & MASK][r]
                    ctr[nums[i] & MASK][1 - r] += 1
                else:
                    ctr[nums[i] & MASK][r] += 1
            MASK |= p
            p //= 2
        return res
    
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        x = {}
        for el in rating:
            x[el] = 0
        for i, el in enumerate(sorted(x)):
            x[el] = i
        for i in range(n):
            rating[i] = x[rating[i]]
        res = 0
        i = 0
        for x, y in zip(self.count(rating, 0), self.count(rating, 1)):
            res += x * y + (i - x) * (n - i - 1 - y)
            i += 1
        return res