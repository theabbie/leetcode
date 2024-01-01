class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        lastone = [-1] * 32
        res = set()
        for i in range(n):
            for b in range(32):
                if arr[i] & (1 << b):
                    lastone[b] = i
            curr = arr[i]
            res.add(curr)
            for j in sorted(lastone, reverse = True):
                if j == -1:
                    break
                curr |= arr[j]
                res.add(curr)
        return len(res)