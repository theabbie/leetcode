import sys

input = sys.stdin.readline

t = int(input())

cres = []

for _ in range(t):
    n, k = map(int, input().split())
    s = list(input().strip())
    for i in range(n):
        diff = ord(s[i]) - ord('a')
        if 26 - diff < diff and k >= 26 - diff:
            s[i] = 'a'
            k -= 26 - diff
            continue
        diff = min(diff, k)
        k -= diff
        s[i] = chr(ord(s[i]) - diff)
    newlast = ord(s[n - 1]) - ord('a')
    if k & 1:
        newlast = min((newlast + 1) % 26, (26 + newlast - 1) % 26)
        s[n - 1] = chr(ord('a') + newlast)
    cres.append("".join(s))

print("\n".join(cres))