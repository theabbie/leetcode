class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        res = [n] * n
        l = {}
        for i in range(2 * n):
            if nums[i % n] in l:
                res[i % n] = min(res[i % n], i - l[nums[i % n]])
                res[l[nums[i % n]] % n] = min(res[l[nums[i % n]] % n], i - l[nums[i % n]])
            l[nums[i % n]] = i
        return [-1 if res[x] == n else res[x] for x in queries]