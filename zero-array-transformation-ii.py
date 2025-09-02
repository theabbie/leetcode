class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        beg = 0
        end = len(queries)
        while beg <= end:
            mid = (beg + end) // 2
            curr = [0] * (n + 1)
            for i in range(mid):
                curr[queries[i][0]] += queries[i][2]
                curr[queries[i][1] + 1] -= queries[i][2]
            for i in range(n):
                curr[i + 1] += curr[i]
            done = True
            for i in range(n):
                if nums[i] > curr[i]:
                    done = False
                    break
            if done:
                end = mid - 1
            else:
                beg = mid + 1
        return end + 1 if end + 1 <= len(queries) else -1