class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        p = [0] * (n + 1)
        res = set()
        for i in range(n):
            p[i + 1] |= p[i] | arr[i]
        for j in range(n - 1, -1, -1):
            res.add(p[j + 1])
            curr = 0
            i = j
            while i >= 0 and curr | p[i + 1] != curr:
                curr |= arr[i]
                res.add(curr)
                i -= 1
        return len(res)