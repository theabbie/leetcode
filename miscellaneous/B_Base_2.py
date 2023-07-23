arr = list(map(int, input().split()))

res = 0

p = 1

for el in arr:
    res += p * el
    p *= 2

print(res)