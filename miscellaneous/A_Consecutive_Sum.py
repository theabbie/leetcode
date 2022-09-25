t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(k):
        j = i
        mval = arr[i]
        while j < n:
            mval = max(mval, arr[j])
            j += k
        res += mval
    print(res)