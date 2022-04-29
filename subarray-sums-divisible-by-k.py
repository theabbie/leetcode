from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        ctr = defaultdict(int)
        ctr[0] += 1
        for num in nums:
            total = (total + num) % k
            ctr[total] += 1
        return sum(n * (n - 1) // 2 for n in ctr.values())