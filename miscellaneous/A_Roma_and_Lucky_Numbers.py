n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in range(n):
    num = arr[i]
    curr = 0
    while num:
        if num % 10 in {4, 7}:
            curr += 1
        num //= 10
    if curr <= k:
        res += 1
print(res)