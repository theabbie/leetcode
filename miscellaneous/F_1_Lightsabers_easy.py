n, m = map(int, input().split())

arr = list(map(int, input().split()))

ctr = list(map(int, input().split()))

ctr = [(i + 1, ctr[i]) for i in range(m)]

i = 0

vals = []

while i < n:
    c = 1
    while i < n - 1 and arr[i] == arr[i + 1]:
        c += 1
        i += 1
    vals.append((arr[i], c))
    i += 1

possible = True

for i in range(len(vals) - len(ctr)):
    matched = True
    for j in range(1, len(ctr) - 1):
        if vals[i + j] != ctr[j]:
            matched = False
            break
    if matched and vals[i][1] <= 0: