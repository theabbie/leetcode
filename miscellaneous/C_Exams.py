n = int(input())

exams = []

for _ in range(n):
    a, b = map(int, input().split())
    exams.append((a, b))

exams.sort()

res = 0

prev = float('-inf')

for i in range(n):
    a, b = sorted(exams[i])
    if a >= prev:
        res = a
    else:
        res = b
    prev = res

print(res)