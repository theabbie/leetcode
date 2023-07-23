t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    lctr = [0] * 26
    uctr = [0] * 26
    for c in s:
        if c.islower():
            lctr[ord(c) - ord('a')] += 1
        else:
            uctr[ord(c) - ord('A')] += 1
    res = 0
    for i in range(26):
        res += min(uctr[i], lctr[i])
        diff = abs(uctr[i] - lctr[i]) // 2
        res += min(diff, k)
        k -= min(diff, k)
    print(res)