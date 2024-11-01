def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        res = 0
        stack = []
        for el in nums[::-1]:
            ns = []
            for g, gctr, s in [(el, 1, el)] + stack:
                if ns and gcd(g, el) == ns[-1][0]:
                    ns[-1][1] += gctr
                    ns[-1][2] += s
                else:
                    ns.append([gcd(g, el), gctr, s])
            pctr = 0
            ps = 0
            for g, gctr, s in ns:
                pctr += gctr
                ps += s
                if pctr >= k:
                    res = max(res, g * ps)
            stack = ns
        return res