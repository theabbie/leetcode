t = int(input())

for _ in range(t):
    n, q = map(int, input().split())

    arr = list(map(int, input().split()))

    res = sum(arr)

    for _ in range(q):
        l, r = map(int, input().split())
        k = r - l + 1
        res += k % 2
    
    print(res)