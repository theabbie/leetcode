import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        k = len(target)
        umask = (1 << k) - 1
        n = len(nums)
        
        v = []
        
        for cmask in range(1, 1 << k):
            l = 1
            for j in range(k):
                if cmask & (1 << j):
                    l = lcm(l, target[j])
            v.append((cmask, l))
        
        dp = [[float('inf')] * (1 << k) for _ in range(n + 1)]
        dp[n][umask] = 0
        
        for i in range(n - 1, -1, -1):
            for mask in range(1 << k):
                dp[i][mask] = dp[i + 1][mask]
                
                val = nums[i]
                for cmask, l in v:
                    new_mask = mask | cmask
                    cost = l * math.ceil(val / l) - val
                    dp[i][mask] = min(dp[i][mask], cost + dp[i + 1][new_mask])
        
        return dp[0][0]