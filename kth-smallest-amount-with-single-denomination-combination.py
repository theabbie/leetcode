class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def lcm(a, b):
            return a * b // gcd(a, b)
        def count(amount):
            res = 0
            for mask in range(1, 1 << n):
                p = 1
                sign = -1
                for i in range(n):
                    if mask & (1 << i):
                        p = lcm(p, coins[i])
                        sign *= -1
                res += sign * (amount // p)
            return res
        end = 1
        while count(end) < k:
            end *= 2
        beg = end // 2
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if count(mid) >= k:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res