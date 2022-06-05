class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return len(set(nums))
        nums.sort()
        subs = [[float('inf'), float('-inf')] for i in range(n)]
        res = 0
        for num in nums:
            for i in range(n):
                mn, mx = subs[i]
                nmn = min(mn, num)
                nmx = max(mx, num)
                if nmx - nmn <= k:
                    subs[i][0], subs[i][1] = nmn, nmx
                    res = max(res, i + 1)
                    break
        return res