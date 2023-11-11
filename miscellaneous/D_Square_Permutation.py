n = int(input())

MAX = pow(10, n)

s = input()

i = 0

res = 0

ctr = [0] * 10
for c in s:
    ctr[int(c)] += 1

while i * i < MAX:
    curr = i * i
    currctr = [0] * 10
    l = 0
    while curr > 0:
        currctr[curr % 10] += 1
        curr //= 10
        l += 1
    currctr[0] += n - l
    if ctr == currctr:
        res += 1
    i += 1

print(res)