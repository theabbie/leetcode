class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] ^= p[i] ^ arr[i]
        res = 0
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if p[j] ^ p[i] == p[k] ^ p[j]:
                        res += 1
        return res