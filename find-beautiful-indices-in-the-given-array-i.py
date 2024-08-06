def compute_lps(pattern):
    length = 0
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def find_pattern_indices(string, pattern):
    indices = []
    n = len(string)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = j = 0

    while i < n:
        if string[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                indices.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        x = find_pattern_indices(s, a)
        y = find_pattern_indices(s, b)
        val = [0] * (n + 1)
        for i in y:
            val[i] = 1
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + val[i]
        res = []
        for i in x:
            ctr = p[min(i + k + 1, n)] - p[max(i - k, 0)]
            if ctr > 0:
                res.append(i)
        return res