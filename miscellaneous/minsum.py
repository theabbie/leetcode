n, x = map(int, input().split())

arr = list(map(int, input().split()))

msum = 0

for el in arr:
    if el >= 0:
        msum += el - el % x
    else:
        msum += el

print(msum)