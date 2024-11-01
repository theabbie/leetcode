class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = 0
        v = [False] * n
        for i in range(n):
            curr = []
            while not v[i]:
                curr.append(arr[i])
                v[i] = True
                i += k
                i %= n
            curr.sort()
            for el in curr:
                res += abs(el - curr[len(curr) // 2])
        return res