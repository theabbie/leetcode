from collections import Counter

n, k = map(int, input().split())

arr = list(map(int, input().split()))

ctr = Counter(arr)

i = 0

rem = k

while i in ctr and rem > 0:
    ctr[i] -= 1
    if ctr[i] == 0:
        del ctr[i]
    i += 1
    rem -= 1

print(i)