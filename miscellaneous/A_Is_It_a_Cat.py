t = int(input())

for _ in range(t):
    n = int(input())
    s = input().lower()
    i = 0
    res = ""
    while i < n:
        while i < n - 1 and s[i] == s[i + 1]:
            i += 1
        res += s[i]
        i += 1
    print("YES" if res == "meow" else "NO")