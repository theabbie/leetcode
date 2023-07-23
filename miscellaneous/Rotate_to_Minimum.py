t = int(input())

for _ in range(t):
    n, p, q = map(int, input().split())
    s = list(input())
    s = [ord(c) - ord('a') for c in s]
    for i in range(n):
        if s[i] <= 13:
            diff = min(s[i], q)
            s[i] -= diff
            q -= diff
        elif p >= 26 - s[i]:
            s[i] = 0
            p -= 26 - s[i]
    print("".join([chr(ord('a') + i) for i in s]))