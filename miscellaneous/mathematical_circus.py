t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    if k % 4 != 0:
        print("YES")
        for i in range(1, n + 1, 2):
            print(i, i + 1)
    else:
        print("NO")