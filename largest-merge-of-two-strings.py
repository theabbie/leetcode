class Solution:
    def largestMerge(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)
        res = []
        i = j = 0
        while i < m and j < n:
            if a[i] > b[j]:
                res.append(a[i])
                i += 1
            elif b[j] > a[i]:
                res.append(b[j])
                j += 1
            else:
                if a[i:] >= b[j:]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
        res.append(a[i:] + b[j:])
        return "".join(res)