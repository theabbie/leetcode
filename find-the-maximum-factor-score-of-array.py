def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        pfg = [0] * (n + 1)
        sfg = [0] * (n + 1)
        pfl = [1] * (n + 1)
        sfl = [1] * (n + 1)
        for i in range(n):
            pfg[i + 1] = gcd(pfg[i], nums[i])
            pfl[i + 1] = lcm(pfl[i], nums[i])
            sfg[i + 1] = gcd(sfg[i], nums[n - i - 1])
            sfl[i + 1] = lcm(sfl[i], nums[n - i - 1])
        res = max(gcd(pfg[i], sfg[n - i - 1]) * lcm(pfl[i], sfl[n - i - 1]) for i in range(n))
        return max(res, pfl[n] * pfg[n])