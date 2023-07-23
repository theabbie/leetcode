n = int(input())

arr = list(map(int, input().split()))

called = [False] * n

for i, el in enumerate(arr):
    if not called[i]:
        called[el - 1] = True

res = []

for i in range(n):
    if not called[i]:
        res.append(i + 1)

print(len(res))
print(*res)