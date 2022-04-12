def nonDivisibleSubset(k, s):
    n = len(s)
    subset = set()
    badPairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if (s[i] + s[j]) % k != 0:
                subset |= {s[i], s[j]}
            else:
                badPairs.append({s[i], s[j]})
    print(subset)
    print(badPairs)
    for bad in badPairs:
        if bad.issubset(subset):
            subset -= bad
    return len(subset)

print(nonDivisibleSubset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]))