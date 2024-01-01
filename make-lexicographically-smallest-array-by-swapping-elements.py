class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        ncp = nums[:]
        vals = sorted([(nums[i], i) for i in range(n)])
        i = 0
        while i < n:
            curr = []
            while i < n - 1 and vals[i + 1][0] - vals[i][0] <= limit:
                curr.append(vals[i][1])
                i += 1
            curr.append(vals[i][1])
            cval = sorted(curr, reverse = True, key = lambda p: ncp[p])
            curr.sort()
            for pos in curr:
                nums[pos] = ncp[cval.pop()]
            i += 1
        return nums