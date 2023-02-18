class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        x = 0
        while x ^ (x >> 1) != start:
            x += 1
        return [i ^ (i >> 1) for i in list(range(x, 1 << n)) + list(range(x))]