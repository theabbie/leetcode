class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        og = nums[:]
        vals = [(el, i) for i, el in enumerate(nums)]
        vals.sort()
        i = 0
        while i < n:
            curr = []
            while i < n - 1 and vals[i + 1][0] - vals[i][0] <= limit:
                curr.append(vals[i][1])
                i += 1
            curr.append(vals[i][1])
            curr.sort()
            poses = sorted(curr, key = lambda x: -og[x])
            for pos in curr:
                nums[pos] = og[poses.pop()]
            i += 1
        return nums