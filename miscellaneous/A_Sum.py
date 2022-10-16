t = int(input())

for _ in range(t):
    a, b, c = sorted(map(int, input().split()))
    if c == a + b:
        print("YES")
    else:
        print("NO")