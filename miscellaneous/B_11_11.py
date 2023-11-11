n = int(input())

res = 0

arr = list(map(int, input().split()))

for i in range(n):
    for j in range(1, arr[i] + 1):
        if len(set(str(i + 1) + str(j))) == 1:
            res += 1

print(res)