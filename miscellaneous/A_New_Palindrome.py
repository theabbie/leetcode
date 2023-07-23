t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    k = n // 2
    a = s[:k]
    b = s[-k:]
    print("YES" if sorted(a) != sorted(b, reverse = True) else "NO")