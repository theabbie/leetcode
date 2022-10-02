class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        p = [(0, 0)]
        for i in range(n):
            e, o = p[-1]
            if i % 2 == 0:
                e += nums[i]
            else:
                o += nums[i]
            p.append((e, o))
        res = 0
        for i in range(n):
            e0, o0 = p[i]
            e1, o1 = p[-1]
            e1 -= e0
            o1 -= o0
            if i % 2 == 0:
                e1 -= nums[i]
            else:
                o1 -= nums[i]
            if e0 + o1 == e1 + o0:
                res += 1
        return res