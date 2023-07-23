t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())
    res = []
    rem = n
    for i in range(k, 0, -1):
        if i != x:
            while i <= rem:
                rem -= i
                res.append(i)
    print(res, rem)
    if rem == 0:
        print("YES")
        print(len(res))
        print(*res)
    else:
        print("NO")