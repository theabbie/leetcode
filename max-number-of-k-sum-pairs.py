from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0
        ctr = Counter(nums)
        for num in ctr:
            if 2 * num <= k and (k - num) in ctr:
                a = ctr[num]
                b = ctr[k - num]
                if 2 * num == k:
                    pairs += a // 2
                else:
                    pairs += min(a, b)
        return pairs