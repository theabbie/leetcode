pals = set()

def check(val):
    if val > 10 ** 9:
        return False
    v = val
    rev = 0
    while val:
        rev = 10 * rev + val % 10
        val //= 10
    return v == rev

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    s = f"{a}{b}{c}{d}{e}"
                    for i in range(1, 6):
                        curr = int(s[:i] + s[:i][::-1])
                        if check(curr):
                            pals.add(curr)
                        curr = int(s[:i] + s[:i][:-1][::-1])
                        if check(curr):
                            pals.add(curr)
                        
pals = sorted(pals)
                        
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        M = max(nums)
        nums.sort()
        l = 0
        r = sum(nums)
        res = r
        i = 0
        for p in pals:
            while i < n and nums[i] <= p:
                l += nums[i]
                r -= nums[i]
                i += 1
            res = min(res, p * i - l + r - (n - i) * p)
            if p > M:
                break
        return res