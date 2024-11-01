class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        def solve(arr):
            n = len(arr)
            p = [0] * (n + 1)
            for i in range(n):
                p[i + 1] = p[i] + arr[i]
            res = float('-inf')
            x = defaultdict(lambda: float('inf'))
            for j in range(n):
                res = max(res, p[j + 1] - x[arr[j] - k])
                x[arr[j]] = min(x[arr[j]], p[j])
            return res
        res = max(solve(nums), solve(nums[::-1]))
        if res == float('-inf'):
            res = 0
        return res