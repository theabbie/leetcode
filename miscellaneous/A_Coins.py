t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    if n & 1:
        print("YES" if k & 1 else "NO")
    else:
        print("YES")