from collections import defaultdict, Counter

MAX = 1 + 10 ** 4

v = [False] * MAX
sp = [0] * MAX

for i in range(2, MAX, 2):
    sp[i] = 2

for i in range(3, MAX, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < MAX:
            if not v[j * i]:
                v[j * i] = True
                sp[j * i] = i
            j += 2

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        sums = defaultdict(int)
        for i in range(n):
            curr = 1
            val = i + 1
            primes = Counter()
            while val > 1:
                primes[sp[val]] += 1
                val //= sp[val]
            for p in primes:
                curr *= pow(p, primes[p] % 2)
            sums[curr] += nums[i]
        return max(sums.values())