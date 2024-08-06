class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        c = {}
        def count(x):
            if x == 0:
                return 0
            if x in c:
                return c[x]
            c[x] = x % 2 + count(x // 2)
            return c[x]
        return sorted(arr, key = lambda x: (count(x), x))