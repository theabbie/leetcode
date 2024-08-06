cache = {}

class Solution:
    def waysToReachStair(self, k: int) -> int:
        def count(i, k, jump, lused):
            if i >= k + 2:
                return 0
            key = (k - i, jump, lused)
            if key in cache:
                return cache[key]
            res = int(i == k)
            if i > 0 and not lused:
                res += count(i - 1, k, jump, True)
            res += count(i + pow(2, jump), k, jump + 1, False)
            cache[key] = res
            return res
        return count(1, k, 0, False)