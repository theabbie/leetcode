x, n = map(int, input().split())

arr = list(map(int, input().split()))

ogarr = arr[::-1]

arr.append(0)
arr.append(x)

n += 2

arr.sort()

pos = {}

for i in range(n):
    pos[arr[i]] = i

res = []

for el in ogarr:
    

print(*res[::-1])