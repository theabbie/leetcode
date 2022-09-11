t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = sum(arr) - n
    if d < 0:
        print(1)
    else:
        print(d)