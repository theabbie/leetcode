t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = [0, 0]
    for el in arr:
        ctr[el % 2] += el
    print("YES" if ctr[0] > ctr[1] else "NO")