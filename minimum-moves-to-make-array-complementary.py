class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        i, j = 0, n - 1
        vals = Counter()
        freq = [0] * (2 * limit + 2)
        while i < j:
            a, b = min(nums[i], nums[j]), max(nums[i], nums[j])
            vals[a + b] += 1
            freq[a + 1] += 1
            freq[b + limit + 1] -= 1
            i += 1
            j -= 1
        for i in range(2 * limit + 1):
            freq[i + 1] += freq[i]
        res = float('inf')
        for i in range(2, 2 * limit + 1):
            one = freq[i] - vals[i]
            two = n // 2 - freq[i]
            res = min(res, one + 2 * two)
        return res