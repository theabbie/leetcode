n = int(input())

arr = list(map(int, input().split()))

pos = [[] for _ in range(4)]

for i in range(n):
    pos[arr[i] - 1].append(i)

ideal = [[] for i in range(4)]

for i in range(n):
    if len(ideal[0]) < len(pos[0]):
        ideal[0].append(i)
    elif len(ideal[1]) < len(pos[1]):
        ideal[1].append(i)
    elif len(ideal[2]) < len(pos[2]):
        ideal[2].append(i)
    elif len(ideal[3]) < len(pos[3]):
        ideal[3].append(i)

print(ideal, pos)