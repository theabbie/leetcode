t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = float('inf')
    for i in range(26):
        curr = 0
        for j in range(n):
            if ord(s[j]) - ord('a') != (i + j) % 26:
                curr += 1
        res = min(res, curr)
    print(res)