n = int(input())

names = []

minage = float('inf')

for _ in range(n):
    name, age = input().split()
    age = int(age)
    names.append((name, age))
    minage = min(minage, age)

i = 0
while names[i][1] != minage:
    i += 1

res = []

for j in range(i, i + n):
    res.append(names[j % n][0])

print("\n".join(res))
