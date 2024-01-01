from collections import Counter

def mos_algorithm(arr, queries):
    block_size = int(math.sqrt(len(arr)))
    sorted_queries = sorted(queries, key=lambda x: x[0] // block_size)
    left, right, dctr = 0, -1, 0
    ctr = [0] * 26
    def remove(x):
        nonlocal dctr
        ctr[x] -= 1
        if ctr[x] == 0:
            dctr -= 1
    def add(x):
        nonlocal dctr
        ctr[x] += 1
        if ctr[x] == 1:
            dctr += 1
    res = 0
    for query_left, query_right in sorted_queries:
        while left > query_left:
            left -= 1
            add(arr[left])
        while right < query_right:
            right += 1
            add(arr[right])
        while left < query_left:
            remove(arr[left])
            left += 1
        while right > query_right:
            remove(arr[right])
            right -= 1
        res += dctr
    return res

class Solution:
    def countPalindromicSubsequence(self, s):
        s = [ord(c) - ord('a') for c in s]
        n = len(s)
        f = [-1] * 26
        l = [-1] * 26
        for i in range(n):
            if f[s[i]] == -1:
                f[s[i]] = i
            l[s[i]] = i
        inv = []
        for x in range(26):
            if f[x] + 1 < l[x]:
                inv.append((f[x] + 1, l[x] - 1))
        return mos_algorithm(s, inv)