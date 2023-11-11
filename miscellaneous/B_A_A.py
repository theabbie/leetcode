n = int(input())

res = 1

while pow(res, res) < n:
    res += 1

if pow(res, res) == n:
    print(res)
else:
    print(-1)