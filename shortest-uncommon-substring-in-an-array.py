from collections import Counter

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        subset = Counter()
        for s in arr:
            n = len(s)
            for i in range(n):
                for j in range(i, n):
                    x = s[i:j+1]
                    subset[x] += 1
        res = [""] * len(arr)
        for pos, s in enumerate(arr):
            n = len(s)
            for i in range(n):
                for j in range(i, n):
                    x = s[i:j+1]
                    subset[x] -= 1
            for i in range(n):
                for j in range(i, n):
                    x = s[i:j+1]
                    if subset[x] == 0:
                        if res[pos] == "":
                            res[pos] = x
                        elif len(x) < len(res[pos]):
                            res[pos] = x
                        elif len(x) == len(res[pos]) and x < res[pos]:
                            res[pos] = x
            for i in range(n):
                for j in range(i, n):
                    x = s[i:j+1]
                    subset[x] += 1
        return res