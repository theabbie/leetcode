from collections import Counter

def kPeriodic(s, k):
    n = len(s)
    if len(set(s)) == 1 or k == 0:
        return s
    p = None
    if n % k == 0:
        p = n // k
    elif n % (n - k) == 0:
        p = n // (n - k)
    else:
        return ""
    ctr = Counter(s)
    res = ""
    for c in sorted(ctr):
        if ctr[c] % p == 0:
            res += c * (ctr[c] // p)
        else:
            return ""
    res *= p
    return res

print(kPeriodic("abcdabcdab", 6))
