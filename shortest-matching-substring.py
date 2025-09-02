def compute_lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    
    occurrences = []
    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences

class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        if p == '**':
            return 0
        n = len(s)
        m = len(p)
        p = p.split("*")
        p = [el for el in p if el]
        if len(p) == 1:
            if p[0] in s:
                return len(p[0])
            return -1
        if len(p) == 2:
            res = float('inf')
            a = kmp(s, p[0])
            b = kmp(s, p[1])
            a.sort()
            i = 0
            for j in b:
                while i < len(a) and a[i] + len(p[0]) - 1 < j:
                    res = min(res, j + len(p[1]) - a[i])
                    i += 1
            if res == float('inf'):
                res = -1
            return res
        a = kmp(s, p[0])
        b = kmp(s, p[1])
        c = kmp(s, p[2])
        res = float('inf')
        for i in b:
            curr = len(p[0]) + len(p[1]) + len(p[2])
            f = i
            l = f + len(p[1]) - 1
            beg = 0
            end = len(a) - 1
            e = False
            while beg <= end:
                mid = (beg + end) // 2
                if a[mid] + len(p[0]) - 1 < f:
                    e = True
                    beg = mid + 1
                else:
                    end = mid - 1
            if not e:
                continue
            curr += f - a[beg - 1] - len(p[0])
            beg = 0
            end = len(c) - 1
            e = False
            while beg <= end:
                mid = (beg + end) // 2
                if c[mid] > l:
                    e = True
                    end = mid - 1
                else:
                    beg = mid + 1
            if not e:
                continue
            curr += c[end + 1] - l - 1
            res = min(res, curr)
        if res == float('inf'):
            return -1
        return res