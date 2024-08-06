class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = list(map(int, digits))
        cache = {}
        def count(num, i, tight, nzseen):
            if i >= len(num):
                return int(nzseen)
            key = (i, tight, nzseen)
            if key in cache:
                return cache[key]
            maxd = 9
            if tight:
                maxd = int(num[i])
            res = 0
            for d in ([] if nzseen else [0]) + digits:
                if d > maxd:
                    break
                res += count(num, i + 1, tight and d == maxd, nzseen or d != 0)
            cache[key] = res
            return res
        return count(str(n), 0, True, False)