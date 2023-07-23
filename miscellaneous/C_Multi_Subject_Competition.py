n, m = map(int, input().split())

students = [[] for _ in range(m)]

for _ in range(n):
    s, r = map(int, input().split())
    students[s - 1].append(r)

mlen = 0

for i in range(m):
    students[i].sort(reverse = True)
    mlen = max(mlen, len(students[i]))
    for j in range(1, len(students[i])):
        students[i][j] += students[i][j - 1]

res = [0] * mlen
    
for i in range(m):
    for j in range(len(students[i])):
        res[j] += max(students[i][j], 0)

print(max(res))