n, t = input().split()

n = int(n)

sl = []

for _ in range(n):
    sl.append(input())

maxpref = [0] * n
maxsuff = [0] * n

for i in range(n):
    m = len(sl[i])
    for c in sl[i]:
        if maxpref[i] < len(t) and c == t[maxpref[i]]:
            maxpref[i] += 1
    j = len(t) - 1
    for c in sl[i][::-1]:
        if j >= 0 and c == t[j]:
            j -= 1
            maxsuff[i] += 1

res = 0

maxsuff.sort()

for i in range(n):
    lower = len(t) - maxpref[i]
    beg = 0
    end = n - 1
    curr = 0
    while beg <= end:
        mid = (beg + end) // 2
        if maxsuff[mid] >= lower:
            curr = n - mid
            end = mid - 1
        else:
            beg = mid + 1
    res += curr

print(res)