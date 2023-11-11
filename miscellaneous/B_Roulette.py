n = int(input())

people = []

for _ in range(n):
    cn = int(input())
    people.append(list(map(int, input().split())))

x = int(input())

vals = []
minpos = float('inf')

for i in range(n):
    if x in people[i]:
        curr = len(people[i])
        minpos = min(minpos, curr)
        vals.append((curr, i + 1))

vals = [vals[i][1] for i in range(len(vals)) if vals[i][0] == minpos]

print(len(vals))

if len(vals) > 0:
    print(*vals)