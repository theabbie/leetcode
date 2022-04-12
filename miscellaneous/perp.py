class Solution:
    def isPerpendicular(self, a: list, b: list, c: list, d: list):
        return (a[0] - b[0]) * (c[1] - d[1]) == (a[1] - b[1]) * (c[0] - d[0])

print(Solution().isPerpendicular([1, 2], [2, 3], [3, 4], [4, 5]))